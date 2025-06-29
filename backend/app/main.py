from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from app import qdrant_client
from app.search import search_chapters

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Biology LLM backend is running"}

@app.get("/search")
def search(query: str = Query(..., min_length=1)):
    return {"results": search_chapters("biology_11", query)}
