# APIRouter lets us create an API route.HTTPException lets us return an error if something goes wrong.
from fastapi import APIRouter, HTTPException 


from app.schemas.query import QueryRequest, QueryResponse
from app.services.retrieval import retrieve_documents
from app.services.generation import generate_answer

# This creates a router where we'll put our API endpoints.
router = APIRouter()

# When someone sends a POST request to /query, run the function below.
@router.post("/query", response_model=QueryResponse)
def query_rag(request: QueryRequest):

    try:
        # Retrieve relevant chunks from ChromaDB
        results = retrieve_documents(
            request.question
        )

        # Generate an answer using the retrieved chunks
        answer, sources = generate_answer(
            request.question,
            results
        )

        return QueryResponse(
            answer=answer,
            sources=sources
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )