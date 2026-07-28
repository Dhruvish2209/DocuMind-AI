import streamlit as st

from utils.suggested_questions import generate_suggested_questions


def render_suggested_questions():

    st.header("Suggested Questions")
    st.caption("Explore AI-generated questions to better understand your uploaded documents.")
    st.divider()

    # Check Documents
    if st.session_state["vector_store"] is None:
        st.info("Upload one or more documents to generate suggested questions.")
        return

    # Session State
    if "suggested_questions" not in st.session_state:
        st.session_state["suggested_questions"] = None

    # Actions
    regenerate = st.button(
        "Regenerate Questions",
        use_container_width=True,
    )

    # Generate Questions
    if (
        st.session_state["suggested_questions"] is None
        or regenerate
    ):

        with st.spinner("Generating suggested questions..."):

            document_text = "\n\n".join(
                page["text"]
                for page in st.session_state["documents"]
            )

            st.session_state["suggested_questions"] = (
                generate_suggested_questions(document_text)
            )

    # Empty State
    if not st.session_state["suggested_questions"]:
        st.warning("No suggested questions could be generated from the uploaded documents.")
        return


    # Display Questions
    for index, question in enumerate(
        st.session_state["suggested_questions"],
        start=1,
    ):
        st.markdown(f"**{index}.** {question}")