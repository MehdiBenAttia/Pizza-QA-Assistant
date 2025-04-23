from huggingface_hub import InferenceClient
import streamlit as st
from vector import retriever
import sys
from dotenv import load_dotenv
import os

load_dotenv()


st.set_page_config(page_title="Pizza QA Assistant", layout="centered")


# Set up the client
client = InferenceClient(
    provider=os.getenv("HF_PROVIDER"),
    api_key=os.getenv("HF_API_KEY"),
)

# Prompt template
template = """
You are an expert in answering questions about a pizza restaurant.

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}
"""

# Streamlit UI
st.title("🍕 Pizza Restaurant QA")

question = st.text_input("Ask a question about the restaurant:")

if question:
    with st.spinner("Thinking..."):
        # Use retriever to get relevant reviews
        reviews = retriever.invoke(question)

        # Format the prompt
        prompt = template.format(reviews=reviews, question=question)

        # Send the prompt to the model
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3-0324",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=512,
        )

        # Show response
        st.subheader("Answer:")
        st.write(response.choices[0].message.content)
