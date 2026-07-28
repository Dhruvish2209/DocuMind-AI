import json

from utils.ai_service import ask_gemini


def generate_quiz(document_text: str):
    """
    Generate multiple-choice quiz questions from the uploaded document(s).
    """

    prompt = f"""
You are an expert educator.

Generate 10 multiple-choice questions based on the following document.

Return ONLY valid JSON.

Format:

[
    {{
        "question": "...",
        "options": [
            "...",
            "...",
            "...",
            "..."
        ],
        "answer": "..."
    }}
]

Rules:
- Exactly 10 questions
- Four options per question
- One correct answer
- No markdown
- No explanations
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