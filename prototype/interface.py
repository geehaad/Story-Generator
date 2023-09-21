import sys
import os
import gradio as gr 
from src.handler import format_output

# Create a Gradio interface
iface = gr.Interface(
    fn=format_output,
    inputs=[
        #Story Genre
        gr.inputs.Dropdown(
            label="Select a Genre",
            choices=["Mystery", "Fantasy", "Science Fiction", "Romance", "Adventure", "Comedy"]
        ),
        #Story Length
        gr.inputs.Slider(
            minimum=5,
            maximum=500,
            step=30,
            default=250,
            label="Story Length (Words)",
        ),
        #Additional information
        gr.inputs.Textbox(label="Enter a story starter, or something you want to be included in the story, exp: story characters"),
    ],

    outputs=gr.outputs.Textbox(label="Generated Story"),
    title="Interactive Story Generator",
    theme= 'huggingface',
    css="footer {visibility: hidden}"
)


# Launch the Gradio interface
iface.launch(auth = ('gehad', 'gehadG1234A@#'),  auth_message="Enter your username and password", share=True)

#The main character is a girl and called Heba