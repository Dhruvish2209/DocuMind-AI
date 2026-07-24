import re


def clean_text(text: str) -> str:
    """
    Clean extracted document text while preserving paragraph structure.
    """

    if not text:
        return ""

    # Remove extra spaces and tabs
    text = re.sub(r"[ \t]+", " ", text)

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove excessive blank lines (keep max 2)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()