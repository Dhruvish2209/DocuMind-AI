import fitz  # PyMuPDF
from docx import Document


def extract_text(uploaded_file):
    """
    Extract text from PDF, DOCX, or TXT files.
    Returns extracted text as a string.
    """

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_pdf(uploaded_file)

    elif file_name.endswith(".docx"):
        return extract_docx(uploaded_file)

    elif file_name.endswith(".txt"):
        return extract_txt(uploaded_file)

    else:
        raise ValueError("Unsupported file format.")


def extract_pdf(uploaded_file):
    text = ""

    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    for page in pdf:
        text += page.get_text()

    return text.strip()


def extract_docx(uploaded_file):
    document = Document(uploaded_file)

    text = "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
    )

    return text.strip()


def extract_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8").strip()