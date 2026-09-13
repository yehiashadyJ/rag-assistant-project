Backend terminal paste and run:
 1.source .venv/bin/activate
 2.PYTHONPATH=backend uvicorn app.main:app --reload

Frontend terminal paste and run: 
 1.source .venv/bin/activate
 2.export API_BASE_URL="http://127.0.0.1:8000"
 3.streamlit run frontend/app.py


 # RAG Document Assistant

A Retrieval-Augmented Generation (RAG) document assistant for
Artificial Intelligence, Machine Learning, and Deep Learning
technical documents.

The system retrieves relevant information from the documents and
uses the local Llama 3.2 model to generate grounded answers with
source references.

## Features

- PDF document processing
- Text extraction
- Fixed-size text chunking
- Text embeddings
- ChromaDB vector store
- Semantic document retrieval
- Llama 3.2 local LLM
- FastAPI backend
- Streamlit frontend
- Answers with source documents
- RAG evaluation using 10 questions

## Architecture

Documents
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
ChromaDB
↓
User Question
↓
Document Retrieval
↓
Llama 3.2
↓
Answer + Sources

## Technologies

- Python 3.10
- FastAPI
- Streamlit
- ChromaDB
- Sentence Transformers
- Ollama
- Llama 3.2
- PyPDF
- Pytest

## RAG Configuration

- Chunk size: 1000 characters
- Chunk overlap: 200 characters
- Embedding model: all-MiniLM-L6-v2
- Embedding dimensions: 384
- Vector database: ChromaDB
- Retrieved chunks: 5
- LLM: Llama 3.2

## Project Structure

```text
rag-assistant-project/
├── backend/
│   ├── app/
│   ├── data/
│   ├── tests/
│   └── requirements.txt
├── frontend/
├── notebooks/
├── data/
├── .gitignore
└── README.md