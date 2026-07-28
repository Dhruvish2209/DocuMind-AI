import os
from dotenv import load_dotenv
from google import genai
from config import MODEL_NAME

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def ask_gemini(context, question, chat_history=""):

    prompt = f"""
You are DocuMind AI, a document question-answering assistant.

Your job is to answer ONLY using the retrieved document context.

Rules:
1. Use the conversation history only to understand follow-up questions.
2. Do NOT use conversation history as factual knowledge.
3. Answer ONLY from the retrieved context.
4. If the answer is not present in the retrieved context, say:
"I couldn't find that information in the uploaded document(s)."
5. Do not hallucinate or invent facts.

Conversation History

{chat_history}

Retrieved Context

{context}

Current Question

{question}
"""

    response = client.models.generate_content(
    model=MODEL_NAME,
    contents=prompt,
    )

    return response.text