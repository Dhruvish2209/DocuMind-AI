import streamlit as st


DEFAULT_SESSION_STATE = {
    "chunks": None,
    "embeddings": None,
    "vector_store": None,
    "bm25": None,

    "documents": [],
    "current_files": [],

    "messages": [],

    "executive_summary": None,
    "key_points": None,
    "flashcards": None,
    "quiz": None,
    "suggested_questions": None,
}


def initialize_session_state() -> None:
    """Initialize Streamlit session state."""

    for key, value in DEFAULT_SESSION_STATE.items():

        if key not in st.session_state:

            st.session_state[key] = value