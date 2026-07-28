import json

from utils.ai_service import ask_gemini


def generate_flashcards(document_text: str):
    """
    Generate flashcards from uploaded document(s).
    """

    prompt = f"""
You are an expert educator.

Generate 10 high-quality study flashcards from the following document.

Return ONLY valid JSON.

Format:

[
    {{
        "question": "...",
        "answer": "..."
    }}
]

Rules:
- Exactly 10 flashcards
- Clear questions
- Short answers
- No explanations outside JSON
- Do not use markdown
- Do not wrap in ```json

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