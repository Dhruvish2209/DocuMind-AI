import streamlit as st

from utils.file_reader import extract_text
from utils.text_cleaner import clean_text
from utils.text_splitter import split_text
from utils.embeddings import get_embeddings
from utils.vector_store import create_vector_store
from utils.bm25_store import create_bm25
from utils.ui import section_header


def render_uploader() -> None:
    """Render the document uploader and process uploaded files."""

    section_header(
        "Upload Documents",
        "Upload PDF, DOCX or TXT files to build your AI workspace.",
    )

    uploaded_files = st.file_uploader(
        label="Choose PDF, DOCX or TXT files",
        type=["pdf", "docx", "txt"],
        accept_multiple_files=True,
        help="Supported formats: PDF, DOCX, TXT",
    )

    if not uploaded_files:
        return

    current_files = sorted(file.name for file in uploaded_files)

    # Skip processing if the same files are already loaded
    if current_files == st.session_state["current_files"]:
        return

    with st.spinner("Building AI workspace..."):

        all_documents = []
        all_chunks = []

        for uploaded_file in uploaded_files:

            # Extract text
            pages = extract_text(uploaded_file)

            # Clean text
            cleaned_pages = clean_text(pages)

            # Store cleaned pages
            all_documents.extend(cleaned_pages)

            # Split into chunks
            chunks = split_text(cleaned_pages)

            all_chunks.extend(chunks)

        # Create embeddings
        texts = [
            chunk["text"]
            for chunk in all_chunks
        ]

        embeddings = get_embeddings(texts)

        # Create vector store
        vector_store = create_vector_store(embeddings)

        # Create BM25 index
        bm25 = create_bm25(all_chunks)

        # Save processed data
        st.session_state["documents"] = all_documents
        st.session_state["chunks"] = all_chunks
        st.session_state["embeddings"] = embeddings
        st.session_state["vector_store"] = vector_store
        st.session_state["bm25"] = bm25
        st.session_state["current_files"] = current_files

        # Reset chat history
        st.session_state["messages"] = []

        # Clear cached AI outputs
        st.session_state["executive_summary"] = None
        st.session_state["key_points"] = None
        st.session_state["flashcards"] = None
        st.session_state["quiz"] = None
        st.session_state["suggested_questions"] = None

    st.success(
        f"Successfully processed {len(uploaded_files)} document(s)."
    )

    with st.expander("Uploaded Files", expanded=True):
        for file_name in current_files:
            st.write(f"✓ {file_name}")