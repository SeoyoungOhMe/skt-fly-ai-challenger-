import gradio as gr
import random
import time
import openai
openai.api_key = "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"

completion = openai.Completion.create(
    model="davinci:ft-apptools-2023-05-01-09-28-53",
    prompt="3박4일 놀러가고 싶다",
    max_tokens=30,
    temperature=0,
)

print(completion['choices'][0]['text'])