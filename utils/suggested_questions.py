import json

from utils.ai_service import ask_gemini


def generate_suggested_questions(document_text: str):
    """
    Generate suggested questions for the uploaded document(s).
    """

    prompt = f"""
You are an expert tutor.

Generate 10 useful questions that a user could ask about the uploaded document.

Return ONLY valid JSON.

Format:

[
    "Question 1",
    "Question 2",
    "Question 3"
]

Rules:
- Exactly 10 questions
- Questions should encourage deeper understanding
- Do not answer the questions
- No markdown
- Return JSON only

Document:

{document_text}
"""

    response = ask_gemini(
        context=document_text,
        question=prompt,
        chat_history=""
    )

    try:
        return json.loads(response)
    except Exception:
        return []