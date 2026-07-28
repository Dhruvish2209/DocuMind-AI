from typing import Any

from utils.embeddings import get_embeddings
from utils.vector_store import search_vector_store
from utils.bm25_store import search_bm25
from utils.rank_fusion import reciprocal_rank_fusion
from utils.reranker import rerank_chunks
from config import RETRIEVE_TOP_K, RERANK_TOP_K

def retrieve_chunks(
    question: str,
    index: Any,
    bm25: Any,
    chunks: list[dict],
    retrieve_top_k=RETRIEVE_TOP_K,
    rerank_top_k=RERANK_TOP_K,
):
    """
    Hybrid Retrieval

    FAISS
        +
    BM25
        ↓
    Reciprocal Rank Fusion
        ↓
    Cross Encoder Reranking
        ↓
    Top Chunks
    """

    query_embedding = get_embeddings([question])[0]

    distances, faiss_indices = search_vector_store(
        index=index,
        query_embedding=query_embedding,
        top_k=retrieve_top_k,
    )

    bm25_results = search_bm25(
        bm25,
        question,
        top_k=retrieve_top_k,
    )

    fused_indices = reciprocal_rank_fusion(
        faiss_indices,
        bm25_results,
    )

    retrieved_chunks = [
        chunks[idx]
        for idx in fused_indices[:retrieve_top_k]
        ]

    reranked_chunks = rerank_chunks(
        question,
        retrieved_chunks,
        top_k=rerank_top_k,
    )

    return {
        "chunks": reranked_chunks,
        "faiss_indices": faiss_indices,
        "distances": distances,
    }