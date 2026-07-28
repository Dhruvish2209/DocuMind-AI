import streamlit as st

from utils.file_reader import extract_text
from utils.text_cleaner import clean_text
from utils.text_splitter import split_text
from utils.embeddings import get_embeddings
from utils.vector_store import create_vector_store
from utils.bm25_store import create_bm25


def process_documents(uploaded_files) -> None:
    """
    Process uploaded documents and initialize the AI workspace.
    """

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

    # Generate embeddings
    texts = [
        chunk["text"]
        for chunk in all_chunks
    ]

    embeddings = get_embeddings(texts)

    # Build retrieval indexes
    vector_store = create_vector_store(embeddings)
    bm25 = create_bm25(all_chunks)

    current_files = sorted(
        file.name
        for file in uploaded_files
    )

    # Save processed data
    st.session_state["documents"] = all_documents
    st.session_state["chunks"] = all_chunks
    st.session_state["embeddings"] = embeddings
    st.session_state["vector_store"] = vector_store
    st.session_state["bm25"] = bm25
    st.session_state["current_files"] = current_files

    # Reset chat
    st.session_state["messages"] = []

    # Clear cached AI outputs
    st.session_state["executive_summary"] = None
    st.session_state["key_points"] = None
    st.session_state["flashcards"] = None
    st.session_state["quiz"] = None
    st.session_state["suggested_questions"] = None