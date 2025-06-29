from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

# Connect to Qdrant
client = QdrantClient(
    host="localhost",
    port=6333,
)

# Define the collection name
COLLECTION_NAME = "biology_11"

# This will DELETE the collection if it exists and create a fresh one
def recreate_collection():
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,  # This must match your embedding model
            distance=Distance.COSINE
        )
    )
    print(f"Collection '{COLLECTION_NAME}' has been recreated (old data deleted).")

# Run this if the script is executed directly
if __name__ == "__main__":
    recreate_collection()
