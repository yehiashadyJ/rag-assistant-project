# We're putting the important settings of our RAG backend in one place:

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ollama_model: str = "llama3.2"
    vector_store_path: str = "backend/data/vector_store"
    collection_name: str = "rag_documents"
    retrieval_count: int = 5

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()