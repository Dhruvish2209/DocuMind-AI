import streamlit as st

from utils.summary import generate_summary


def render_summary():

    st.header("Executive Summary")
    st.caption("A concise AI-generated overview of your uploaded documents.")
    st.divider()

    # Check Documents
    if st.session_state["vector_store"] is None:
        st.info("Upload one or more documents to generate an executive summary.")
        return

    # Session State
    if "executive_summary" not in st.session_state:
        st.session_state["executive_summary"] = None

    # Actions
    _, col = st.columns([4, 1])

    with col:

        regenerate = st.button(
            "Regenerate",
            use_container_width=True
        )

    # Generate Summary
    if (
        st.session_state["executive_summary"] is None
        or regenerate
    ):

        with st.spinner("Generating executive summary..."):

            document_text = "\n\n".join(
                page["text"]
                for page in st.session_state["documents"]
            )

            st.session_state["executive_summary"] = generate_summary(
                document_text
            )

    # Display Summary
    st.markdown(st.session_state["executive_summary"])