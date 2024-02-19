# This is based on https://huggingface.co/spaces/Abbasid/TableQA

from transformers import pipeline
import pandas as pd
import gradio as gr

tqa = pipeline(task="table-question-answering", model="google/tapas-large-finetuned-wtq")

query = "what is the highest delta onu rx power?"

def main(filepath, query):

  tableau = pd.read_csv(filepath).astype(str)
  result = tqa(table=tableau, query=query)["answer"]
  return result


iface = gr.Interface(
    fn=main,
    inputs=[
        gr.File(type="filepath", label="Upload csv"),
        gr.Textbox(type="text", label="What do you want to know?"),
    ],
    outputs=[gr.Textbox(type="text", label="The output will be here" , lines=3)]
)

# Launch the Gradio interface
iface.launch()