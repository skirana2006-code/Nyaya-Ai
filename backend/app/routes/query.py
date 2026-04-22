from fastapi import APIRouter, HTTPException
from app.services.embedding_service import generate_embeddings
from app.services.vector_db_service import query_embeddings

router = APIRouter()


@router.post("/query")
async def query_docs(query: str):
    """
    Query stored documents
    """

    try:
        # Step 1: Convert query to embedding
        query_embedding = generate_embeddings([query])[0]

        # Step 2: Search DB
        results = query_embeddings(query_embedding)

        return {
            "query": query,
            "results": results
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))