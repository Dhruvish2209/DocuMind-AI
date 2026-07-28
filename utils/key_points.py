from utils.ai_service import ask_gemini


def generate_key_points(document_text: str) -> str:
    """
    Generate key takeaways from the uploaded document(s).
    """

    prompt = f"""
You are an expert document analyst.

Extract the most important key takeaways from the following document(s).

Requirements:
- Return 8-15 important points.
- Use bullet points.
- Keep each point concise.
- Include only important information.
- Do not repeat similar ideas.
- Do not invent information.

Document:

{document_text}
"""

    key_points = ask_gemini(
        context=document_text,
        question=prompt,
        chat_history=""
    )

    return key_points.strip()