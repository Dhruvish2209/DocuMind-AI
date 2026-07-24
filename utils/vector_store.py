import faiss
import numpy as np


def create_vector_store(embeddings):
    """
    Create a FAISS index from embedding vectors.

    Args:
        embeddings: Numpy array of embeddings.

    Returns:
        FAISS index.
    """

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index

def search_vector_store(index, query_embedding, top_k=3):
    """
    Search the FAISS index.

    Args:
        index: FAISS index
        query_embedding: Embedding of user's question
        top_k: Number of results

    Returns:
        distances, indices
    """

    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    return distances, indices