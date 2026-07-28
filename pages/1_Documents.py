import streamlit as st

from components.sidebar import render_sidebar
from components.workspace import (
    render_workspace_header,
    render_document_overview,
)
from components.uploader import render_uploader
from components.ai_tools import render_ai_tool
from utils.session import initialize_session_state


# Initialize session state
initialize_session_state()


# Sidebar
with st.sidebar:
    selected_tool = render_sidebar()


# Main page
render_workspace_header()

render_document_overview()

render_uploader()

st.divider()

render_ai_tool(selected_tool)