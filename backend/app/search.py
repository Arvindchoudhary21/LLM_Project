from app.embeddings import get_embedding
from app.qdrant_client import client, COLLECTION_NAME

def search_chapters(collection_name: str, query: str, top_k: int = 3):
    # Step 1: Convert search text to embedding
    vector = get_embedding(query)

    # Step 2: Query Qdrant for similar vectors
    search_result = client.search(
        collection_name=collection_name,
        query_vector=vector,
        limit=top_k
    )

    # Step 3: Format and return results
    results = []
    for hit in search_result:
        results.append({
            "title": hit.payload["title"],
            "content": hit.payload["content"][:500] + "",  # show a preview
            "score": round(hit.score, 3)  # similarity score
        })

    return results
