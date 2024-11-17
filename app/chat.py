from .llm_handler import generate_response
from typing import List

def handle_query(prompt: str, knowledge_base: List[str]):
    # Generate a response based on the combined documents in knowledge_base
    response = generate_response(prompt, knowledge_base)
    return response
