import os
import streamlit as st
from huggingface_hub import InferenceClient

# Page settings
st.set_page_config(
    page_title="Traditional LLM Chatbot",
    page_icon="🤖"
)

# Title
st.title("🤖 Traditional LLM Chatbot")
st.write("Ask a question and get an answer from the LLM.")

# Hugging Face client
client = InferenceClient(
    api_key=os.environ["HF_TOKEN"]
)

# Question input
question = st.text_input("Enter your question:")

# Button
if st.button("Ask AI"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:
        with st.spinner("Generating answer..."):

            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            answer = response.choices[0].message.content

        st.subheader("🤖 AI Answer")
        st.write(answer)