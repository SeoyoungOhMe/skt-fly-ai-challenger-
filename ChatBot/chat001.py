import gradio as gr
import openai
openai.api_key = "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"

def greet(name):
    completion = openai.ChatCompletion.creat(
        model = "gpt-3.5-turbo", messages=[{"role": "user", "content": content+"한글로 번역해줘"}]
    )
    return completion.choices[0].message.content

demo = gr.Interface(fn=greet, inputs="text", outputs = "text")

demo.launch(share=True)


import openai
import gradio as gr

openai.api_key = "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"

def greet(content):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": content + " 한글로 번역해줘" }
    ]
    )
    return completion.choices[0].message.content

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch(share=True)   