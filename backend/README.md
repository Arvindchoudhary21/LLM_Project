# Backend

step 1: Set up the project

Created a Python project folder named backend

Created core files:

main.py -> (FastAPI app)

qdrant_utils.py -> (Qdrant setup & insert)

search.py -> (semantic search function)

embeddings.py -> (embedding model)

data_loader.py -> (to uplaod the data to the qdrant database)

Step 2: Installed All Packages from requirements.txt  
Instead of installing each manually with pip install, we used:

pip install -r requirements.txt

This command:  
•	Reads each line in requirements.txt  
•	Installs all packages (and their dependencies)  
•	Ensures clean, consistent setup on any machine  

✅ fastapi
Purpose:
Used to build the backend API — for example:
•	/search endpoint for intelligent search
•	Handling HTTP requests/responses
•	Creating routes for search, health check, etc.
Why we chose it:
Fast, modern, async-ready, and Pythonic — perfect for REST APIs.

✅ uvicorn
Purpose:
This is the ASGI server used to run the FastAPI app.
Command used:
uvicorn main:app --reload

Why we chose it:
Required to serve FastAPI with live reloading in development.

✅ qdrant-client
Purpose:
Used to connect with the Qdrant vector database, including:
•	Creating a collection (biology-chapters)
•	Uploading embeddings to Qdrant
•	Performing semantic search with search() API

Why we chose it:
It’s the official Python client for Qdrant.

✅ sentence-transformers
Purpose:
To generate semantic vector embeddings from chapter content using the model:
all-MiniLM-L6-v2
Example:
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding = model.encode(text)

Why we chose it:
Lightweight, fast, accurate — works well for sentence-level embeddings.


✅ 1. Created the FastAPI App (main.py).

We initialized a FastAPI app to serve our API routes.

✅ 2. Loaded SentenceTransformer (embeddings.py)

We used sentence-transformers and the model: all-MiniLM-L6-v2 to convert text to vector embeddings.

✅ 3. Created qdrant_client.py

✅ Purpose of this file:
•	Connects to Qdrant
•	Recreates the "biology_11" collection with vector size 384 and COSINE distance
•	Used before inserting embeddings into the DB.

✅ 4. Loaded and Inserted Data (data_loader.py)

This loaded your chapters or definitions and inserted embeddings.

✅ 5. Created search.py

✅ This handled the intelligent semantic search:
•	Embeds the user query
•	Searches Qdrant using client.search
•	Returns title, previewed content, and score

✅ 6. Connected search.py in FastAPI (main.py)

We called search_chapters() inside /search endpoint and returned top matches.

✅ 7. Ran the API Server

uvicorn main:app --reload

And you tested via Postman or browser at:

http://localhost:8000/search



# How sentence-transformers/all-MiniLM-L6-v2 working

🧠 ✅ LLM in Your Project: What It’s Doing
The LLM is used to enable intelligent search — so when a user types a query (like “genus” or “what is taxonomy”), the system doesn't just look for exact words, but understands the meaning of the query and returns the most semantically relevant answer from the database.

1. Backend Prepares the Data
✅ We have:

•	A file definitions.json or chapters.json with title + content
•	Each text is converted into a vector (embedding) using a pretrained LLM-based model all-MiniLM-L6-v2.

📌 Model Details:

Feature	Description

Name	                sentence-transformers/all-MiniLM-L6-v2
Type	                Transformer-based (LLM-powered embedding model)
Vector Size	            384 dimensions
Training Objective	    Trained on semantic similarity and sentence-pair tasks
Speed	                Very fast and lightweight (ideal for local use)
From	                Hugging Face / Microsoft (via sentence-transformers)
Library Used	        sentence-transformers Python library

🔍 What It Does
This model is not a chat-style LLM like GPT, but it is built using transformer layers, making it part of the LLM family of models.
It is specially fine-tuned to:
•	Convert any sentence, paragraph, or short document
•	Into a fixed-size semantic embedding vector
•	Which can be compared using cosine similarity

✅ Why it's a Good Choice
•	Lightweight (runs locally)
•	Fast to load and process
•	Delivers great performance for semantic search
•	Works perfectly with Qdrant vector database

2. What LLM Are You Using?
We are using the all-MiniLM-L6-v2 model from Hugging Face via sentence-transformers.
This model is not a full GPT-type LLM, but a sentence-level transformer trained to:
✨ Convert a piece of text into a fixed-size vector that captures its meaning
So it’s LLM-powered embeddings, not full natural language generation.

3. Embeddings Go Into Qdrant
•	Those vectors are stored in a vector database: Qdrant
•	Each vector is tied to a title, content, and chapter_id

4. User Types a Query
•	The query (e.g., “what is genus?”) is also sent to the same embedding model → converted to a vector

5. Qdrant Does Vector Similarity Search
Qdrant compares the query vector to all the stored vectors using cosine similarity.
🔍 It finds the most similar vector (i.e., content semantically close to the user’s question)

6. Backend Sends Top Result to Frontend
•	The top result (title + content) is returned from FastAPI
•	Displayed on frontend in a ChapterCard component

📌 Example
❌ Without LLM:
•	Search "what is genus" → it would match only chapters containing the exact word "genus"
✅ With LLM:
•	Search "group of related species" → it would still match the definition of genus, because the model understands the meaning




