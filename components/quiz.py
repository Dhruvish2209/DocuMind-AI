import streamlit as st

from utils.quiz import generate_quiz


def render_quiz():

    st.header("Quiz")
    st.caption("Test your understanding with AI-generated multiple-choice questions.")
    st.divider()

    # -----------------------------------------
    # Check Documents
    # -----------------------------------------

    if st.session_state["vector_store"] is None:
        st.info("Upload one or more documents to generate a quiz.")
        return

    # -----------------------------------------
    # Session State
    # -----------------------------------------

    if "quiz" not in st.session_state:
        st.session_state["quiz"] = None

    # -----------------------------------------
    # Actions
    # -----------------------------------------

    regenerate = st.button(
        "Regenerate Quiz",
        use_container_width=True,
    )

    # -----------------------------------------
    # Generate Quiz
    # -----------------------------------------

    if (
        st.session_state["quiz"] is None
        or regenerate
    ):

        with st.spinner("Generating quiz..."):

            document_text = "\n\n".join(
                page["text"]
                for page in st.session_state["documents"]
            )

            st.session_state["quiz"] = generate_quiz(
                document_text
            )

    # -----------------------------------------
    # Empty State
    # -----------------------------------------

    if not st.session_state["quiz"]:
        st.warning("No quiz questions could be generated from the uploaded documents.")
        return

    # -----------------------------------------
    # Display Quiz
    # -----------------------------------------

    for index, question in enumerate(st.session_state["quiz"], start=1):

        st.subheader(f"Question {index}")

        user_answer = st.radio(
            question["question"],
            question["options"],
            key=f"quiz_{index}",
        )

        if st.button(
            f"Check Answer",
            key=f"check_{index}",
            use_container_width=True,
        ):

            if user_answer == question["answer"]:

                st.success("Correct!")

            else:

                st.error(
                    f"Correct Answer: {question['answer']}"
                )

        st.divider()