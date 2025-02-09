# app.py
import gradio as gr
from backend import add_phone_number, list_phone_numbers  # Import backend functions

# Gradio interface
with gr.Blocks() as app:
    gr.Markdown("# Phone Number Database App")

    # Input fields for adding a phone number
    with gr.Row():
        phone_input = gr.Textbox(label="Enter Phone Number (10 digits)", placeholder="e.g.,07891234567")
        additional_input = gr.Textbox(label="Enter Client_code (5 or 6 digits)", placeholder="e.g., 12345")
    add_button = gr.Button("Add Phone Number")
    add_output = gr.Textbox(label="Add Status", interactive=False)

    # Button to list all phone numbers
    list_button = gr.Button("List All Phone Numbers")
    list_output = gr.Textbox(label="Stored Phone Numbers", interactive=False)

    # Link Gradio components to the functions
    add_button.click(fn=add_phone_number, inputs=[phone_input, additional_input], outputs=add_output)
    list_button.click(fn=list_phone_numbers, outputs=list_output)

# Launch the Gradio app
app.launch()
