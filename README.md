# DocuMind-AI

An AI-powered Document Question Answering application built using **Retrieval-Augmented Generation (RAG)**.

Upload a PDF, DOCX, or TXT document and ask questions in natural language. The application retrieves the most relevant content using semantic search and generates grounded answers using Google's Gemini model.

---

## Features

- Upload PDF, DOCX, and TXT files
- Automatic text extraction
- Text cleaning and preprocessing
- Intelligent text chunking
- Sentence Transformer embeddings
- FAISS vector database
- Semantic similarity search
- Gemini Flash powered answers
- Retrieval-Augmented Generation (RAG)

---

## Project Architecture

User Uploads Document
        │
        ▼
Extract Text
        │
        ▼
Clean Text
        │
        ▼
Split into Chunks
        │
        ▼
Generate Embeddings
        │
        ▼
Store in FAISS
        │
        ▼
User Question
        │
        ▼
Question Embedding
        │
        ▼
Semantic Search
        │
        ▼
Retrieve Relevant Context
        │
        ▼
Gemini Flash
        │
        ▼
Final Answer

---

## Project Structure

```
DocuMind-AI/
│
├── Home.py
├── pages/
│   └── 1_Document_Upload.py
│
├── utils/
│   ├── file_reader.py
│   ├── text_cleaner.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── rag.py
│   └── ai_service.py
│
├── uploads/
├── assets/
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### AI / Machine Learning

- Sentence Transformers
- FAISS
- Retrieval-Augmented Generation (RAG)
- Google Gemini API

### Libraries

- PyMuPDF
- python-docx
- NumPy
- python-dotenv
- google-genai

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run Home.py
```

---

## How It Works

1. Upload a document
2. Text is extracted and cleaned
3. Document is divided into chunks
4. Embeddings are generated
5. Embeddings are stored in FAISS
6. User asks a question
7. Similar chunks are retrieved
8. Gemini receives only the retrieved context
9. Grounded answer is generated

---

## Future Improvements

- Multiple document support
- Chat history
- Source citations
- Streaming responses
- Session caching
- Better UI
- Conversation memory

---

## Author

Dhruvish Chudasama

MCA Student | AI & Machine Learning Enthusiast
=======
AI-powered document intelligence system for PDF question answering using Retrieval-Augmented Generation (RAG).
