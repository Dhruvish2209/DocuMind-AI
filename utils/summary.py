from utils.ai_service import ask_gemini


def generate_summary(document_text: str) -> str:
    """
    Generate an executive summary for the uploaded document(s).
    """

    prompt = f"""
You are an expert document analyst.

Generate a professional executive summary of the following document(s).

Requirements:
- Keep it concise and well-structured.
- Focus on the main ideas and important information.
- Use clear, professional language.
- Use bullet points if appropriate.
- Do not invent information.
- If multiple documents are provided, summarize them together.

Document:
{document_text}
"""

    summary = ask_gemini(
        context=document_text,
        question=prompt,
        chat_history=""
    )

    return summary.strip()