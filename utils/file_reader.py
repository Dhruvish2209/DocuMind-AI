import fitz  # PyMuPDF
from docx import Document


def extract_text(uploaded_file):
    """
    Extract text while preserving page information.

    Returns:
        list[dict]

    Example:
    [
        {
            "page": 1,
            "text": "..."
        },
        {
            "page": 2,
            "text": "..."
        }
    ]
    """

    file_extension = uploaded_file.name.split(".")[-1].lower()

    # PDF
    if file_extension == "pdf":

        pdf = fitz.open(
            stream=uploaded_file.read(),
            filetype="pdf"
        )

        pages = []

        for page_number, page in enumerate(pdf, start=1):

            pages.append(
                {
                    "file_name": uploaded_file.name,
                    "page": page_number,
                    "text": page.get_text()
                    }
                )

        pdf.close()

        return pages

    # DOCX
    elif file_extension == "docx":

        document = Document(uploaded_file)

        text = "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )

        return [
            {
                "file_name": uploaded_file.name,
                "page": 1,
                "text": text
                }
                ]

    # TXT
    elif file_extension == "txt":

        text = uploaded_file.read().decode("utf-8")

        return [
            {
                "file_name": uploaded_file.name,
                "page": 1,
                "text": text
            }
            ]

    else:
        raise ValueError("Unsupported file format.")