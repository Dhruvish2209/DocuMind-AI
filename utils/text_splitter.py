def split_text(text: str, chunk_size: int = 500, overlap: int = 100):
    """
    Split text into overlapping chunks.

    Args:
        text (str): Cleaned document text.
        chunk_size (int): Maximum characters per chunk.
        overlap (int): Characters shared between consecutive chunks.

    Returns:
        list[str]: List of text chunks.
    """

    if not text:
        return []

    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk_size.")

    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks