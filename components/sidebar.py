import streamlit as st


def render_sidebar():

    st.title("AI Tools")

    selected_tool = st.radio(
    "Choose a feature",
    [
        "Chat",
        "Executive Summary",
        "Key Takeaways",
        "Flashcards",
        "Quiz Generator",
        "Suggested Questions",
    ],
    key="sidebar_feature_selector",
    )

    st.divider()

    st.subheader("Uploaded Documents")

    if st.session_state["current_files"]:

        for file in st.session_state["current_files"]:

            st.write(f"{file}")

    else:

        st.caption("No documents uploaded.")

    st.divider()

    st.caption("DocuMind AI")
    st.caption("Version 3.1")

    return selected_tool