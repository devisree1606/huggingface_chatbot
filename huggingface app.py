import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"]
)

response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Explain artificial intelligence in simple words."
        }
    ]