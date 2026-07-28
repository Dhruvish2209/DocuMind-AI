from pathlib import Path

import streamlit as st


def load_css() -> None:
    """Load the global stylesheet."""

    css = Path("assets/css/main.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def hero() -> None:
    """Render the application hero section."""

    st.markdown(
        """
        <div class="hero">
            <div class="hero-title">
                DocuMind AI
            </div>
            <div class="hero-subtitle">
                Chat with your documents, generate executive summaries,
                extract key takeaways, create flashcards, build quizzes,
                and explore insights using AI.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def section_header(title: str, subtitle: str | None = None) -> None:
    """Render a reusable section header."""

    st.markdown(f"## {title}")

    if subtitle:
        st.caption(subtitle)


def metric_card(title: str, value: str | int, subtitle: str) -> None:
    """Render a reusable metric card."""

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-subtitle">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )