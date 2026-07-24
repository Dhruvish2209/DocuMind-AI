from utils.embeddings import get_embeddings
from utils.vector_store import search_vector_store


def retrieve_context(question, index, chunks, top_k=3):
    """
    Retrieve the most relevant chunks for a question.
    """

    query_embedding = get_embeddings([question])[0]

    _, indices = search_vector_store(
        index,
        query_embedding,
        top_k
    )

    context = []

    for idx in indices[0]:
        context.append(chunks[idx])

    return "\n\n".join(context)