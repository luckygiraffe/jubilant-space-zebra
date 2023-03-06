import gradio as gr
import openai

def answer(question):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        temperature=0.6,
        max_tokens=150,
    )
    return response["choices"][0]["text"]

gr.Interface(fn=answer, inputs="text", outputs="text").launch()