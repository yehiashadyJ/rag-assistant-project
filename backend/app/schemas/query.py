from pydantic import BaseModel

#This tells FastAPI When someone sends a question to /query, I expect a text question."
class QueryRequest(BaseModel):
    question: str

#his tells FastAPI:"When I respond, I'll send back an answer and a list of sources."
class QueryResponse(BaseModel):
    answer: str
    sources: list[str]