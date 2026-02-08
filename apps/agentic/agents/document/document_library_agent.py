from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage
from langchain.prompts import PromptTemplate

from apps.agentic.core.agents.file_chroma_rag_agent import FileChromaRAGAgent
from apps.agentic.core.document_loaders.document_library_loader import DocumentLibraryLoader
from lib.logger import get_logger

logger = get_logger("YADA")


class DocumentLibraryAgent(FileChromaRAGAgent):
    """
    PDF Document Agent that uses a vector store index of PDF documents to answer questions about document
    content. It is designed to handle queries related to PDF documents like: title, topic, authors, 
    published_date, and shelf.
    """

    QUERY_FILTERS =  """
        **document_library_search Query Filters**
        The agent supports the following query filters to refine searches:
        - authors: Author names (e.g., author:Troy Stribling)
        - topic: Research topic (e.g., topic:AI)
        - published_date: Start date of work on the research note (e.g., date:2023-01-01)
        - shelf: Shelf associated with the document (e.g., shelf:reading_list)

        **Example Filtered Queries**
        - title: Thermodynamics Look in the document library for the definition of a Carnot Cycle.
        - author:Troy Stribling What documents in the document library discuss Thermodynamics?
        - published_date:2023-01-01 What documents in the document library discuss Thermodynamics?
        - shelf:publications Look in the document library for the definition of a Carnot Cycle
    """

    def __init__(self, query):
        tool_name = "document_library_agent_tool"
        tool_description = """
            PDF Document Retriever
            Description: Search and retrieve content from the PDF document library which contains
            indexed PDF documents that cover a wide range of technical and research topics
            Use this for any query about 'document library', 'library' or 'PDF documents'.
        """

        prompt_template = """
            You are searching the PDF document library in his indexed library vector store to answer
            requests about the contents of the documents. Information about the document can be found 
            in the metadata attached to each file.
            Following is a description of the metadata.
            - Document filename: {metadata[filename]}
            - Document file path: {metadata[path]}
            - Document title: {metadata[title]}
            - Document published date: {metadata[published_date]}
            - Document authors: {metadata[authors]}
            - Document topic description: {metadata[topic]}
            - Document shelf: {metadata[shelf]}
            ---
            {page_content}
        """
        
        document_prompt = PromptTemplate.from_template(template=prompt_template)

        super().__init__(tool_name, tool_description, document_prompt, DocumentLibraryLoader(), query)


    def read_file(self, top_files):
        """
        Reconstruct and return the full file contents of the **top** retrieved PDF
        by pulling all of its chunks from the Chroma collection and ordering them.

        Ordering preference:
          1) If 'page' is present in metadata -> sort by page (int) then stable index
          2) Else if ('section','section_char_offset') -> (section, section_char_offset)
          3) Else if 'start_index' -> start_index
          4) Else preserve retrieval order

        Returns a markdown string that includes a small metadata header and a
        fenced block containing the reconstructed text. If nothing can be found,
        returns an empty string.
        """
        try:
            if not top_files:
                return ""

            # Use the first unique file/path from the top hits
            top = top_files[0]
            md0 = top.metadata or {}
            path = md0.get("path")
            filename = md0.get("filename")

            vs = self.doc_loader.vectorstore
            coll = getattr(vs, "_collection", None)
            if coll is None:
                return ""

            where = {"path": str(path)} if path else ({"filename": str(filename)} if filename else None)
            if not where:
                return ""

            # Pull all chunks for the file
            try:
                res = coll.get(where=where, include=["documents", "metadatas"], limit=100_000, offset=0)
            except Exception as e:
                logger.error(f"Error fetching full file from collection: {e}")
                return ""

            docs = res.get("documents") or []
            metas = res.get("metadatas") or []
            if not docs:
                return ""

            # Build sortable tuples
            items = []
            any_page = False
            any_section = False
            for i, (txt, md) in enumerate(zip(docs, metas)):
                txt = txt or ""
                m = md or {}
                page = m.get("page")
                section = m.get("section")
                sec_off = m.get("section_char_offset") or 0
                start_ix = m.get("start_index") or 0
                if page is not None:
                    any_page = True
                    try:
                        page = int(page)
                    except Exception:
                        page = 0
                    items.append(((0, page, i), txt, m))
                elif section is not None:
                    any_section = True
                    try:
                        sec_off = int(sec_off)
                    except Exception:
                        sec_off = 0
                    items.append(((1, str(section), sec_off, i), txt, m))
                elif start_ix is not None:
                    try:
                        start_ix = int(start_ix)
                    except Exception:
                        start_ix = i
                    items.append(((2, start_ix, i), txt, m))
                else:
                    items.append(((3, i), txt, m))

            items.sort(key=lambda t: t[0])

            # Compose output with simple page/section dividers
            out_parts = []
            header_bits = []
            title = md0.get("title") or ""
            authors = md0.get("authors") or ""
            published = md0.get("published_date") or ""
            topic = md0.get("topic") or ""
            shelf = md0.get("shelf") or ""

            header_bits.append(f"**File:** {filename or path or '(unknown)'}")
            if path:
                header_bits.append(f"**Path:** {path}")
            if title:
                header_bits.append(f"**Title:** {title}")
            if authors:
                header_bits.append(f"**Authors:** {authors}")
            if published:
                header_bits.append(f"**Published:** {published}")
            if topic:
                header_bits.append(f"**Topic:** {topic}")
            if shelf:
                header_bits.append(f"**Shelf:** {shelf}")

            header = "\n".join(header_bits)

            current_marker = None
            for key, txt, m in items:
                if any_page:
                    marker = f"Page {key[1]}"  # key = (0, page, i)
                elif any_section:
                    marker = str(m.get("section") or "")
                else:
                    marker = None

                if marker and marker != current_marker:
                    out_parts.append(f"\n\n--- {marker} ---\n\n")
                    current_marker = marker
                out_parts.append(txt)

            body = "".join(out_parts).strip()

            if not body:
                return ""

            # Wrap in a fenced block so it renders monospaced without mangling math
            out = [
                "\n\n-----\n\n",
                header,
                "\n\n",
                "```text\n",
                body,
                "\n```\n"
            ]
            return "".join(out)

        except Exception as e:
            logger.error(f"read_file failed: {e}")
            return ""


    def _generate(self, state):
        """
        Generate an answer for PDF-library queries.
        Includes:
        - normal RAG answer
        - optional file dump via read_file(top_files)
        - pdf_hint {path, pages[]} so UI can render iframe + page chips
        """

        messages = state["messages"]
        question = messages[0].content
        last_message = messages[-1]
        docs = last_message.content

        # 1. try to build files_section (full file dump or clamped)
        files_section = ""
        pdf_hint = None
        try:
            hits = self.retriever.invoke(question)

            # pick top file for full dump
            seen, top_files = set(), []
            for d in hits:
                path = (d.metadata or {}).get("path")
                if not path or path in seen:
                    continue
                seen.add(path)
                top_files.append(d)
                if len(top_files) >= 1:
                    break

            files_section = self.read_file(top_files) or ""

            # collect PDF metadata
            by_path_pages = {}
            for d in hits:
                meta = d.metadata or {}
                pth = meta.get("path")
                if not pth:
                    continue
                pages_meta = meta.get("pages") or meta.get("page")
                if isinstance(pages_meta, int):
                    page_list = [pages_meta]
                elif isinstance(pages_meta, list):
                    page_list = [pg for pg in pages_meta if isinstance(pg, int)]
                else:
                    page_list = []
                if pth not in by_path_pages:
                    by_path_pages[pth] = set()
                for pg in page_list:
                    by_path_pages[pth].add(pg)

            # choose first path
            for d in hits:
                meta = d.metadata or {}
                pth = meta.get("path")
                if pth and pth in by_path_pages:
                    pdf_hint = {
                        "path": pth,
                        "pages": sorted(by_path_pages[pth]) if by_path_pages[pth] else None,
                    }
                    break

        except Exception as e:
            logger.error(f"PDF Agent file expansion failed: {e}")
            files_section = ""
            pdf_hint = None

        # 2. run RAG prompt to get answer_text
        prompt = hub.pull("rlm/rag-prompt")
        rag_chain = prompt | self.llm | StrOutputParser()
        answer_text = rag_chain.invoke({"context": docs, "question": question})

        # 3. build base final_text (what you want the user to read)
        final_text = answer_text + (files_section if files_section else "")

        # 4. append pdf_hint footer in-band as JSON, if present
        if pdf_hint:
            import json
            hint_json = json.dumps(pdf_hint)
            final_text = (
                final_text
                + "\n\n```json\n__PDF_HINT_START__\n"
                + hint_json
                + "\n__PDF_HINT_END__\n```\n"
            )

        # 5. return a NORMAL AIMessage so LangGraph stays happy
        return {
            "messages": [
                AIMessage(content=final_text)
            ]
        }
