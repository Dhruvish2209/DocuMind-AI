import streamlit as st

from utils.key_points import generate_key_points


def render_key_points():

    st.header("Key Takeaways")
    st.caption("The most important insights extracted from your uploaded documents.")
    st.divider()

    # Check Documents
    if st.session_state["vector_store"] is None:
        st.info("Upload one or more documents to extract key takeaways.")
        return

    # Session State
    if "key_points" not in st.session_state:
        st.session_state["key_points"] = None

    # Actions
    _, col = st.columns([4, 1])

    with col:

        regenerate = st.button(
            "Regenerate",
            use_container_width=True
        )

    # Generate Key Takeaways
    if (
        st.session_state["key_points"] is None
        or regenerate
    ):

        with st.spinner("Extracting key takeaways..."):

            document_text = "\n\n".join(
                page["text"]
                for page in st.session_state["documents"]
            )

            st.session_state["key_points"] = generate_key_points(
                document_text
            )

    # Display Key Takeaways
    st.markdown(st.session_state["key_points"])