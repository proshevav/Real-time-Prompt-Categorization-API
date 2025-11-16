import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/classify"
st.title("Real-Time Prompt Categorization")

prompt = st.text_area("Type your prompt:")

if prompt:
    response = requests.post(API_URL, json={"prompt": prompt})

    if response.status_code == 200:
        data = response.json()

        st.subheader("Predicted Categories:")
        for category in data["categories"]:
            st.write(f"{category['name']} (Confidence: {category['confidence']:.2f})")

        st.subheader("Recommended LLM Settings:")
        settings = data["settings"]
        for key, value in settings.items():
            st.write(f"{key}: {value}")
    else:
        st.error("Failed to get response from the API. Please try again.")
