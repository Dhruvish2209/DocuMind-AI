from typing import Any

from utils.retriever import retrieve_chunks


def retrieve_context(
    question: str,
    index: Any,
    bm25: Any,
    chunks: list[dict],
):
    """
    Build context from retrieved chunks.
    Retrieval logic lives in retriever.py.
    """

    result = retrieve_chunks(
        question=question,
        index=index,
        bm25=bm25,
        chunks=chunks,
    )

    retrieved_chunks = result["chunks"]

    context_parts = []
    sources = []
    retrieval_debug = []

    seen_sources = set()

    for chunk in retrieved_chunks:

        context_parts.append(chunk["text"])

        source_key = (
            chunk["file_name"],
            chunk["page"],
        )

        if source_key not in seen_sources:

            sources.append(
                {
                    "file_name": chunk["file_name"],
                    "page": chunk["page"],
                }
            )

            seen_sources.add(source_key)

        retrieval_debug.append(
            {
                "file_name": chunk["file_name"],
                "page": chunk["page"],
                "preview": chunk["text"][:250],
            }
        )

    context = "\n\n".join(context_parts)

    return context, sources[:2], retrieval_debug