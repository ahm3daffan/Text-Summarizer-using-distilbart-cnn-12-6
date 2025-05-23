# Import necessary libraries
import torch
import gradio as gr
from accelerate.commands.config.update import description  # (Optional import, not used in this script)
from transformers import pipeline

# Define the path to the locally downloaded Hugging Face model (distilbart-cnn-12-6)
# Make sure the model is placed at this path or update it as needed
model_path = "../Models/models--sshleifer--distilbart-cnn-12-6/snapshots/a4f8f3ea906ed274767e9906dbaede7531d660ff"

# Load the summarization pipeline with the specified model
# torch_dtype=bfloat16 is used for performance on compatible hardware (like newer NVIDIA GPUs)
# device=0 indicates usage of the first GPU (if available)
textsummary = pipeline(
    "summarization",
    model=model_path,
    torch_dtype=torch.bfloat16,
    device=0
)

# Define the summarization function to be called by Gradio
def summary(input):
    # Get the model's summary output for the input text
    output = textsummary(input)
    # Return only the summary text portion from the output dictionary
    return output[0]['summary_text']

# Close any previously running Gradio interfaces (helpful during development)
gr.close_all()

# Create the Gradio interface
demo = gr.Interface(
    fn=summary,  # Function to call when user submits text
    inputs=[gr.Textbox(label="Input text to summarize")],  # Input textbox for user text
    outputs=[gr.Textbox(label="Output text to summarize", lines=4)],  # Output textbox to display the summary
    title="Summarizing text",  # Title of the app
    description="This application will be used to summarize the input text."  # Description shown below the title
)

# Launch the Gradio web interface
demo.launch()
z
