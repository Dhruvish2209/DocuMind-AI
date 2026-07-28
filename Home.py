import streamlit as st

from utils.ui import load_css, hero

st.set_page_config(
    page_title="DocuMind AI",
    layout="wide",
)

load_css()

hero()

st.divider()

st.markdown(
    '<div class="section-title">Everything You Need</div>',
    unsafe_allow_html=True,
)

col1,col2,col3=st.columns(3)

with col1:

    st.markdown("""
    <div class="feature-card">
    <div class="feature-title">Chat</div>
    <div class="feature-text">
    Ask natural questions about your uploaded documents.
    </div>
    </div>
    """,unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="feature-card">
    <div class="feature-title">Executive Summary</div>
    <div class="feature-text">
    Generate concise summaries in seconds.
    </div>
    </div>
    """,unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="feature-card">
    <div class="feature-title">Flashcards</div>
    <div class="feature-text">
    Turn documents into interactive study cards.
    </div>
    </div>
    """,unsafe_allow_html=True)