"""
Global configuration for DocuMind AI.
Update values here instead of changing them across the project.
"""

# Gemini
MODEL_NAME = "gemini-flash-latest"

# Text Splitting
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

# Retrieval
RETRIEVE_TOP_K = 15
RERANK_TOP_K = 5

# Chat
MAX_CHAT_HISTORY = 6


# Summary
SUMMARY_LENGTH = 250