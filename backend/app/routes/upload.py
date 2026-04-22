from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdf_service import extract_text_from_pdf
from backend.app.services.vector_db_service import chunk_text
from app.services.embedding_service import generate_embeddings
from app.services.vector_db_service import chunk_text
router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):    
    """
    Upload a PDF file, extract text, clean it,
    chunk it, and return chunks.
    """

    # Validate file type
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    try:
        # Step 1: Extract raw text
        text = extract_text_from_pdf(file)

        # Step 2: Chunk text
        chunks = chunk_text(text, chunk_size=500, overlap=50)

        return {
            "message": "PDF processed successfully",
            "total_chunks": len(chunks),
            "chunks": chunks
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 

