from fastapi import APIRouter, HTTPException
from app.services.embedding_service import generate_embeddings
from app.services.vector_db_service import query_embeddings
from app.services.llm_service import generate_answer

router = APIRouter()


@router.post("/query")
async def query_docs(query: str):
    """
    Query documents and generate answer
    """

    try:
        # Step 1: Embed query
        query_embedding = generate_embeddings([query])[0]

        # Step 2: Retrieve relevant chunks
        chunks = query_embeddings(query_embedding)

        # Step 3: Generate answer using LLM
        answer = generate_answer(query, chunks)

        return {
            "query": query,
            "answer": answer,
            "context_used": chunks
        }

    except Exception as e:
        print("ERROR:", e) 
        raise HTTPException(status_code=500, detail=str(e))