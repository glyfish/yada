import sys, os, json, time, warnings; warnings.filterwarnings("ignore")
sys.path.insert(0, "/Users/troy/Develop/gly.fish/yada"); os.chdir("/Users/troy/Develop/gly.fish/yada")
from dotenv import load_dotenv; load_dotenv("/Users/troy/Develop/gly.fish/yada/.env")
os.environ["LANGCHAIN_TRACING_V2"] = "false"
from typing import cast
from langchain_core.messages import HumanMessage
from apps.agentic.agents.document.research_library_agent import ResearchLibraryAgent
from apps.agentic.core.agents.chroma_rag_agent import ChunkRanking
SEP = "\n\n-----\n\n"
OUT = "/private/tmp/claude-501/-Users-troy-Develop-gly-fish-yada/f1f2eee9-96e3-40ce-bfa8-e62d3f23046a/scratchpad/floor_data.json"

a = ResearchLibraryAgent(query={})
coll = a.doc_loader.vectorstore._collection
metas = [m for m in (coll.get(limit=coll.count(), include=["metadatas"]).get("metadatas") or []) if m]

# one (topic -> title) pair per document; topic is the query, title is ground truth
pairs = {}
for m in metas:
    if m.get("title") and m.get("topic") and m["title"] not in pairs:
        pairs[m["title"]] = m["topic"]
print(f"  {len(pairs)} labelled queries", flush=True)

ranker = a._grade_prompt | a._grader_llm
rows = []
t0 = time.time()
for i, (title, topic) in enumerate(sorted(pairs.items()), 1):
    try:
        hits = a.retriever.invoke(topic)
        if not hits: continue
        ctx = SEP.join(f"Document {j}:\n{h.page_content}" for j, h in enumerate(hits, 1))
        r = cast(ChunkRanking, ranker.invoke({"question": topic, "documents": ctx}))
        scored = {s.index: s.score for s in r.scores if 1 <= s.index <= len(hits)}
        rows.append({
            "title": title, "query": topic[:120],
            "scores":  [round(scored.get(j, 0.0), 3) for j in range(1, len(hits)+1)],
            "correct": [h.metadata.get("title") == title for h in hits],
        })
    except Exception as e:
        print(f"    [{i}] {title[:40]}: {type(e).__name__}", flush=True)
    if i % 10 == 0: print(f"    {i}/{len(pairs)}  {time.time()-t0:.0f}s", flush=True)
json.dump(rows, open(OUT, "w"), indent=1)
print(f"\n  collected {len(rows)} query vectors in {time.time()-t0:.0f}s -> {OUT}")
