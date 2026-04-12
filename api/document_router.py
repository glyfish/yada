from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import Response

from pathlib import Path

from lib.logger import get_logger

router = APIRouter()
logger = get_logger("YADA")

DOCUMENT_LIBRARY_DIR = Path("./document_library").resolve()


"""
Stream specified PDF document
"""
@router.get("/document/stream_pdf_document")
async def serve_pdf(
    name: str = Query(..., description="basename of the PDF, e.g. foo.pdf")
):
    """
    Return a PDF in a browser-displayable way (no download prompt).
    The front end calls this like:
      /api/document/pdf?name=Discrete%20State%20Markov%20Chain%20Equilibrium.pdf
    """

    safe_name = Path(name).name
    if safe_name != name:
        raise HTTPException(status_code=400, detail="Invalid filename")

    pdf_path = (DOCUMENT_LIBRARY_DIR / safe_name).resolve()

    if not str(pdf_path).startswith(str(DOCUMENT_LIBRARY_DIR)):
        raise HTTPException(status_code=400, detail="Invalid filename")

    if not pdf_path.exists() or not pdf_path.is_file():
        raise HTTPException(status_code=404, detail="PDF not found")

    data = pdf_path.read_bytes()

    return Response(
        content=data,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'inline; filename="{safe_name}"',
            "Cache-Control": "no-store",
        },
    )
