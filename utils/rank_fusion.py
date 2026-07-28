from collections import defaultdict


def reciprocal_rank_fusion(
    faiss_indices,
    bm25_results,
    k=60,
):
    """
    Combine FAISS and BM25 rankings using
    Reciprocal Rank Fusion (RRF).

    Returns:
        List[int] -> fused chunk indices
    """

    scores = defaultdict(float)

    # FAISS ranking
    for rank, chunk_index in enumerate(faiss_indices[0], start=1):

        scores[int(chunk_index)] += 1 / (k + rank)

    # BM25 ranking
    for rank, (chunk_index, _) in enumerate(bm25_results, start=1):

        scores[int(chunk_index)] += 1 / (k + rank)

    ranked = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    return [
        chunk_index
        for chunk_index, _ in ranked
    ]