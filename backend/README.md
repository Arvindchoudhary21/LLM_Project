Backend Project Setup and Overview
Project Setup
Step 1: Project Structure
Created a Python project folder named backend with the following core files:

main.py: FastAPI application
qdrant_utils.py: Qdrant setup and data insertion
search.py: Semantic search functionality
embeddings.py: Embedding model configuration
data_loader.py: Data upload to Qdrant database

Step 2: Package Installation
Installed all required packages using:
pip install -r requirements.txt

This command ensures a consistent setup by installing all dependencies listed in requirements.txt.
Installed Packages

fastapiPurpose: Builds the backend API, handling HTTP requests/responses and creating routes (e.g., /search endpoint, health check).Why: Fast, modern, async-ready, and Pythonic, ideal for REST APIs.

uvicornPurpose: ASGI server to run the FastAPI app with live reloading in development.Command: uvicorn main:app --reloadWhy: Essential for serving FastAPI applications.

qdrant-clientPurpose: Connects to Qdrant vector database for creating collections (e.g., biology-chapters), uploading embeddings, and performing semantic searches.Why: Official Python client for Qdrant.

sentence-transformersPurpose: Generates semantic vector embeddings using the all-MiniLM-L6-v2 model.Example:
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding = model.encode(text)

Why: Lightweight, fast, and accurate for sentence-level embeddings.


Step 3: Implementation Details

FastAPI App (main.py)Initialized a FastAPI app to serve API routes.

SentenceTransformer (embeddings.py)Used sentence-transformers with the all-MiniLM-L6-v2 model to convert text to vector embeddings.

Qdrant Client (qdrant_utils.py)  

Connects to Qdrant.  
Creates the biology_11 collection with vector size 384 and COSINE distance.  
Used before inserting embeddings into the database.


Data Loading (data_loader.py)Loaded chapters or definitions and inserted their embeddings into Qdrant.

Semantic Search (search.py)  

Embeds user queries.  
Searches Qdrant using client.search.  
Returns title, previewed content, and similarity score.


API Integration (main.py)Integrated search_chapters() into the /search endpoint to return top matches.

Running the APIStarted the server with:
uvicorn main:app --reload

Tested via Postman or browser at: http://localhost:8000/search.


How Semantic Search Works with all-MiniLM-L6-v2
Overview
The all-MiniLM-L6-v2 model enables intelligent semantic search, understanding the meaning of queries (e.g., “genus” or “what is taxonomy”) rather than relying on exact word matches.
Workflow

Data Preparation  

Text data (e.g., definitions.json or chapters.json) is converted into 384-dimensional vector embeddings using all-MiniLM-L6-v2.  
Model Details:  
Name: sentence-transformers/all-MiniLM-L6-v2  
Type: Transformer-based embedding model  
Vector Size: 384 dimensions  
Training Objective: Semantic similarity and sentence-pair tasks  
Speed: Lightweight and fast for local use  
Source: Hugging Face via sentence-transformers library




Embedding Storage  

Vectors are stored in Qdrant, tied to title, content, and chapter_id.


Query Processing  

User queries (e.g., “what is genus?”) are converted to vectors using the same model.


Vector Similarity Search  

Qdrant compares the query vector to stored vectors using cosine similarity to find semantically similar content.


Result Delivery  

FastAPI returns the top result (title + content) to the frontend, displayed in a ChapterCard component.



Why all-MiniLM-L6-v2?

Lightweight and runs locally.  
Fast processing and loading.  
High performance for semantic search.  
Seamless integration with Qdrant.

Example

Without LLM: Searching “what is genus” matches only exact instances of “genus”.  
With LLM: Searching “group of related species” matches the definition of genus by understanding semantic similarity.
