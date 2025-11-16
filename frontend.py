import streamlit as st
import requests
import time

API_URL = "http://127.0.0.1:5000/classify"

st.title("Real-Time Prompt Categorization")

if "last_input_time" not in st.session_state:
    st.session_state.last_input_time = time.time()
    st.session_state.prompt = ""

def get_debounced_input(input_text):
    DEBOUNCE_DELAY = 0.3

    current_time = time.time()

    if current_time - st.session_state.last_input_time > DEBOUNCE_DELAY:
        st.session_state.prompt = input_text
        st.session_state.last_input_time = current_time


prompt = st.text_area("Type your prompt:")

if prompt:
    get_debounced_input(prompt)

if st.session_state.prompt != "":
    response = requests.post(API_URL, json={"prompt": st.session_state.prompt})

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
