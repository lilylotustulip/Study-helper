# NOTE! THE ACTUAL CODE IS IN STUDYHELPER.PY NOT THIS FILE
import os
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# 1. Load the token from the .env file
load_dotenv()
hf_token = os.getenv("HFtoken")

# 2. Initialize the client 
# We use a widely supported model for the Inference API
client = InferenceClient(token=hf_token, model="meta-llama/Llama-3.1-8B-Instruct")
# 3. Streamlit UI
st.title("My Study Helper")
user_input = st.text_input("Enter your notes or question:")

if st.button("Summarize / Ask"):
    if user_input:
        try:
            # 4. Call the API
            messages = [{"role": "user", "content": f"Summarize this: {user_input}"}]
            response = client.chat_completion(messages=messages)
            
            # 5. Display the result
            st.write("### Result:")
            st.write(response.choices[0].message.content)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text first.")
