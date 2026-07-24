import os

from google import genai
from google.genai.errors import ClientError
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(context, question):
    prompt = f"""
You are an AI assistant answering questions about an uploaded document.

Use ONLY the provided context.

If the context contains enough information to answer, answer clearly and concisely.

If the context only partially answers the question, say what the document states and mention that it does not provide further details.

If the answer is completely absent from the context, reply:

"I couldn't find that information in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text

    except ClientError as e:
        return f"Gemini API Error: {e}"