import json
import uuid
from app.embeddings import get_embedding
from app.qdrant_client import client, COLLECTION_NAME
from qdrant_client.http.models import PointStruct

# Step 1: Load definitions from JSON
with open("data/definitions.json", "r", encoding="utf-8") as f:
    definitions = json.load(f)

# Step 2: Prepare and upload each definition to Qdrant
def upload_definitions():
    points = []

    for definition in definitions:
        vector = get_embedding(definition["content"])

        point = PointStruct(
            id=str(uuid.uuid4()),   # Unique ID for this point
            vector=vector,          # Embedding from sentence-transformer
            payload={
                "title": definition["title"],
                "content": definition["content"],
                "chapter": definition["chapter"]
            }
        )

        points.append(point)

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print(f"✅ Uploaded {len(points)} definitions to Qdrant.")

# Step 3: Run if executed directly
if __name__ == "__main__":
    upload_definitions()
