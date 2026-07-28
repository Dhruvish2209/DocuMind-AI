from rank_bm25 import BM25Okapi


def create_bm25(chunks):

    corpus = [
        chunk["text"].lower().split()
        for chunk in chunks
    ]

    return BM25Okapi(corpus)


def search_bm25(
    bm25,
    query,
    top_k=5
):

    scores = bm25.get_scores(
        query.lower().split()
    )

    ranked = sorted(
        enumerate(scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked[:top_k]