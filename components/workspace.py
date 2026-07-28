import streamlit as st

from utils.ui import metric_card, section_header


def render_workspace_header() -> None:
    section_header(
        "Documents",
        "Upload, organize and analyze your documents using AI.",
    )


def render_document_overview() -> None:
    files = len(st.session_state["current_files"])
    pages = len(st.session_state["documents"])
    chunks = len(st.session_state["chunks"] or [])

    ready = st.session_state["vector_store"] is not None

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card("Files", files, "Uploaded")

    with col2:
        metric_card("Pages", pages, "Processed")

    with col3:
        metric_card("Chunks", chunks, "Indexed")

    with col4:
        metric_card(
            "Status",
            "Ready" if ready else "Waiting",
            "AI Workspace",
        )