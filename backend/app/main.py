# This gives us the FastAPI framework.
from fastapi import FastAPI

# CORS allows your frontend and backend to communicate.
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.query import router

# This creates your actual FastAPI application.
app = FastAPI(
    title="RAG Document Assistant",
    description="A RAG-powered AI assistant for technical documents.",
    version="1.0.0"
)


# Allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# checks if the backend running 
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


app.include_router(router)