# app.py

import os
import gradio as gr
import google.generativeai as genai
from dotenv import load_dotenv
from prompts import prompt_examples

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

for model in genai.list_models():
    print(model.name)


# Initialize Gemini model
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-lite")

# === Function to handle prompt and return structured output === #
def run_prompt(prompt_type):
    """
    Given a prompt type (e.g., Zero-Shot), run the corresponding prompt
    through Gemini and return the result.
    """
    prompt = prompt_examples.get(prompt_type, "")
    
    if not prompt:
        return f"No prompt found for type: {prompt_type}", ""

    try:
        response = model.generate_content(prompt)
        return prompt, response.text.strip()
    except Exception as e:
        return prompt, f"Error: {e}"


# === Gradio UI Setup === #
with gr.Blocks(title="Prompt Engineering Playground") as demo:
    gr.Markdown("# 🧠 Prompt Engineering Playground")
    gr.Markdown("Explore Zero-shot, One-shot, Few-shot prompting and see how LLMs behave under different styles.")

    prompt_type = gr.Dropdown(
        choices=list(prompt_examples.keys()),
        label="Select Prompt Type",
        value="Zero-Shot"
    )

    btn = gr.Button("Run Prompt")

    with gr.Row():
        input_prompt = gr.Textbox(label="📝 Prompt Sent to Model", lines=5, interactive=False)
        output_response = gr.Textbox(label="📤 Gemini Response", lines=5)

    btn.click(fn=run_prompt, inputs=prompt_type, outputs=[input_prompt, output_response])

# Launch the app
if __name__ == "__main__":
    
    demo.launch()
