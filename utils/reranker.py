from sentence_transformers import CrossEncoder

# Load once
reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank_chunks(
    question: str,
    chunks: list[dict],
    top_k: int = 5,
):
    """
    Re-rank retrieved chunks using a Cross Encoder.
    """

    pairs = [
        (question, chunk["text"])
        for chunk in chunks
    ]

    scores = reranker.predict(pairs)

    ranked = sorted(
        zip(chunks, scores),
        key=lambda x: x[1],
        reverse=True,
    )

    return [
        chunk
        for chunk, _ in ranked[:top_k]
    ]