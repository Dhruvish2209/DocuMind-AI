import streamlit as st

from config import MAX_CHAT_HISTORY

from utils.rag import retrieve_context
from utils.ai_service import ask_gemini


def render_chat():

    # Check Documents
    if st.session_state["vector_store"] is None:

        st.info("Upload one or more documents to start chatting.")

        return

    # Chat History
    for message in st.session_state["messages"]:

        with st.chat_message(message["role"]):

            st.write(message["content"])

    # Chat Input
    question = st.chat_input(
        "Ask something about your uploaded documents..."
    )

    if not question:
        return

    # Save User Message
    st.session_state["messages"].append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):

        st.write(question)

    # Generate Response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            context, sources, _ = retrieve_context(
                question=question,
                index=st.session_state["vector_store"],
                bm25=st.session_state["bm25"],
                chunks=st.session_state["chunks"],
            )

            if context.strip():

                recent_messages = st.session_state["messages"][
                    -MAX_CHAT_HISTORY:
                ]

                history = "\n\n".join(
                    f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
                    for msg in recent_messages
                )

                answer = ask_gemini(
                    context=context,
                    question=question,
                    chat_history=history,
                )

            else:

                answer = (
                    "I couldn't find relevant information in the uploaded "
                    "documents. Try rephrasing your question or asking about "
                    "another topic."
                )

            st.write(answer)

    # Save Assistant Message
    st.session_state["messages"].append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    st.rerun()