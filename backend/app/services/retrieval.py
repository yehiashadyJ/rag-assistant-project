import chromadb
from sentence_transformers import SentenceTransformer

from app.core.config import settings


# Load the embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


# Connect to the persisted ChromaDB
client = chromadb.PersistentClient(
    path=settings.vector_store_path
)


# Open the existing collection
collection = client.get_collection(
    name=settings.collection_name
)


def retrieve_documents(question: str, n_results: int = None):

    if n_results is None:
        n_results = settings.retrieval_count

    # Convert the user's question into an embedding
    question_embedding = embedding_model.encode(
        question
    ).tolist()

    # Search ChromaDB for similar chunks
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=n_results
    )

    return results