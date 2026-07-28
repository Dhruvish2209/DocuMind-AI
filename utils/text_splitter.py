from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP

def split_text(
    pages: list[dict],
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
) -> list[dict]:
    """
    Split cleaned pages into semantic chunks while preserving metadata.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = []
    chunk_id = 0

    for page in pages:

        page_chunks = splitter.split_text(page["text"])

        for chunk in page_chunks:

            chunks.append(
                {
                    "chunk_id": chunk_id,
                    "file_name": page["file_name"],
                    "page": page["page"],
                    "text": chunk
                }
            )

            chunk_id += 1

    return chunks