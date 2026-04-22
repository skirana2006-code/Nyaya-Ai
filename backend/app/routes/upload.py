from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdf_service import extract_text_from_pdf
from app.services.chunk_service import chunk_text
from app.services.embedding_service import generate_embeddings
from app.services.vector_db_service import store_embeddings

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload PDF → Extract → Chunk → Embed → Store
    """

    # Validate file type
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF allowed")

    try:
        # Step 1: Extract text
        text = extract_text_from_pdf(file)

        # Step 2: Chunk text
        chunks = chunk_text(text)

        # Step 3: Generate embeddings
        embeddings = generate_embeddings(chunks)

        # Step 4: Store in DB
        store_embeddings(chunks, embeddings)

        return {
            "message": "stored successfully",
            "total_chunks": len(chunks)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))