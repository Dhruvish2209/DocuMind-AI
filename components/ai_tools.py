from components.chat import render_chat
from components.summary import render_summary
from components.key_points import render_key_points
from components.flashcards import render_flashcards
from components.quiz import render_quiz
from components.suggested_questions import render_suggested_questions


def render_ai_tool(selected_tool):

    if selected_tool == "Chat":

        render_chat()

    elif selected_tool == "Executive Summary":

        render_summary()

    elif selected_tool == "Key Takeaways":

        render_key_points()

    elif selected_tool == "Flashcards":

        render_flashcards()

    elif selected_tool == "Quiz Generator":

        render_quiz()

    elif selected_tool == "Suggested Questions":

        render_suggested_questions()