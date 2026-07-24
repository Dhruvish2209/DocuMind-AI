import streamlit as st

from utils.file_reader import extract_text
from utils.rag import retrieve_context
from utils.text_cleaner import clean_text
from utils.text_splitter import split_text
from utils.embeddings import get_embeddings
from utils.vector_store import create_vector_store
from utils.ai_service import ask_gemini
st.title("Document Upload")

uploaded_file = st.file_uploader(
    "Upload a document",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:

    try:
        text = extract_text(uploaded_file)
        text = clean_text(text)

        st.success("Document uploaded successfully!")

        st.subheader("Preview")

        st.text_area(
            "Extracted Text",
            text[:2000],
            height=350
        )

        chunks = split_text(text)

        st.success(f"Total Chunks: {len(chunks)}")

        # for i, chunk in enumerate(chunks):
        #     with st.expander(f"Chunk {i+1}"):
        #         st.write(chunk)

        embeddings = get_embeddings(chunks)

        vector_store = create_vector_store(embeddings)

        question = st.text_input("Ask a question")

        if question:

            context = retrieve_context(
                question,
                vector_store,
                chunks
            )
            
            answer = ask_gemini(
                context,
                question
            )

            st.subheader("Answer")
            st.write(answer)

    except Exception as e:
        st.error(f"Error: {e}")