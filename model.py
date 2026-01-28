import random

RESPONSES = [
    "This is a generated response from the language model.",
    "The system processed your input successfully.",
    "Model inference completed with simulated output.",
    "This response demonstrates LLM serving behavior."
]

def generate_text(prompt: str):
    return f"Prompt: {prompt}\nResponse: {random.choice(RESPONSES)}"
