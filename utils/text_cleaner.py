import re
from typing import List


def clean_text(pages: List[dict]) -> List[dict]:
    """
    Clean extracted document text while preserving metadata.

    Args:
        pages (List[dict]):
            List of page dictionaries.

    Returns:
        List[dict]:
            Cleaned pages with metadata preserved.
    """

    cleaned_pages = []

    for page in pages:

        text = page["text"]

        # Remove extra spaces and tabs
        text = re.sub(r"[ \t]+", " ", text)

        # Remove excessive blank lines
        text = re.sub(r"\n\s*\n+", "\n\n", text)

        # Remove leading and trailing whitespace
        text = text.strip()

        cleaned_pages.append(
            {
                "file_name": page["file_name"],
                "page": page["page"],
                "text": text
            }
        )

    return cleaned_pages