# prompts.py
"""
This file contains all the predefined prompts used in the app.
"""

prompt_examples = {
    "Zero-Shot": "What is the capital of France?",

    "One-Shot": """Q: What is the capital of Germany?
A: Berlin
Q: What is the capital of France?""",

    "Few-Shot": """Q: What is the capital of Germany?
A: Berlin
Q: What is the capital of Italy?
A: Rome
Q: What is the capital of France?""",

    "Hallucination": "What is the capital of Wakanda?"
}