from sentence_transformers import SentenceTransformer

# Step 1: Load the pre-trained model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 2: Function to generate embedding for a given text
def get_embedding(text: str) -> list[float]:
    """
    Generate a vector embedding from input text.
    """
    embedding = model.encode(text)
    return embedding.tolist()  # Convert NumPy array to Python list for JSON serialization

