from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embeddings(chunks: list[str]):
    """
    Convert text chunks into embedding vectors.

    Args:
        chunks (list[str]): List of text chunks.

    Returns:
        list: Embedding vectors.
    """

    embeddings = embedding_model.encode(chunks)

    return embeddings