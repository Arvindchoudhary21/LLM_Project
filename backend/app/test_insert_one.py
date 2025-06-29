from app.qdrant_client import client, COLLECTION_NAME
from app.embeddings import get_embedding
from qdrant_client.http.models import PointStruct
import uuid

# Definition we want to insert
definition = {
    "title": "Definition: Genus",
    "content": """Genus comprises a group of related species which has more characters in common in comparison to species of other genera. 
For example, potato and brinjal are two different species but both belong to the genus Solanum. 
Lion, leopard and tiger are species of the genus Panthera, which differs from the genus Felis that includes cats."""
}

# Convert to embedding
vector = get_embedding(definition["content"])

# Prepare point
point = PointStruct(
    id=str(uuid.uuid4()),
    vector=vector,
    payload={
        "title": definition["title"],
        "content": definition["content"]
    }
)

# Insert into Qdrant
client.upsert(
    collection_name=COLLECTION_NAME,
    points=[point]
)

print("Definition uploaded to Qdrant!")
