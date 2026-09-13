# RAG Document Assistant

## Backend terminal — paste and run:

1. Activate the virtual environment:

```bash
source .venv/bin/activate
```

2. Start the FastAPI backend:

```bash
PYTHONPATH=backend uvicorn app.main:app --reload
```

## Frontend terminal — paste and run:

1. Activate the virtual environment:

```bash
source .venv/bin/activate
```

2. Set the backend URL:

```bash
export API_BASE_URL="http://127.0.0.1:8000"
```

3. Start the Streamlit frontend:

```bash
streamlit run frontend/app.py
```

---

## Description

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

```text
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
```

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
- Embedding model: `all-MiniLM-L6-v2`
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
```

## Testing

Run the backend tests:

```bash
PYTHONPATH=backend pytest backend/tests/test_query.py -v
```

The project includes tests for:

- Health endpoint
- Successful RAG query
- Invalid query input

All three tests currently pass.

## Evaluation

The RAG system was evaluated using 10 questions covering different AI and Machine Learning concepts.

The evaluation checks:

- Answer correctness
- Grounding
- Retrieved sources
- Failure cases

The evaluation achieved 9/10 correct and grounded answers in the conducted evaluation.

## Documents

The original source documents are not included in this repository.

They should be provided separately and processed to create the local vector store.

## Future Improvements

- Improve retrieval quality
- Add more evaluation questions
- Improve the user interface
- Deploy the application