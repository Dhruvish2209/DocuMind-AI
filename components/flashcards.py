import streamlit as st

from utils.flashcards import generate_flashcards


def render_flashcards():

    st.header("Flashcards")
    st.caption("Review important concepts using AI-generated question and answer cards.")
    st.divider()

    # Check Documents
    if st.session_state["vector_store"] is None:
        st.info("Upload one or more documents to generate flashcards.")
        return

    # Session State
    if "flashcards" not in st.session_state:
        st.session_state["flashcards"] = None

    # Actions
    regenerate = st.button(
        "Regenerate Flashcards",
        use_container_width=True,
    )

    # Generate Flashcards
    if (
        st.session_state["flashcards"] is None
        or regenerate
    ):

        with st.spinner("Generating flashcards..."):

            document_text = "\n\n".join(
                page["text"]
                for page in st.session_state["documents"]
            )

            st.session_state["flashcards"] = generate_flashcards(
                document_text
            )

    # Empty State
    if not st.session_state["flashcards"]:
        st.warning("No flashcards could be generated from the uploaded documents.")
        return
    
    # Display Flashcards
    for index, card in enumerate(
        st.session_state["flashcards"],
        start=1,
    ):

        with st.expander(f"Flashcard {index}"):

            st.markdown("**Question**")
            st.write(card["question"])

            st.divider()

            st.markdown("**Answer**")
            st.write(card["answer"])