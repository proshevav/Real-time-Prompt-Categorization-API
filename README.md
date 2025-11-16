# Real-Time Prompt Categorization API

This project provides a real-time prompt categorization service that classifies user input prompts into relevant categories. It also recommends optimal LLM (Language Model) settings based on the identified categories.

## Features

- **Real-time prompt classification**: Classifies user prompts into multiple relevant categories (e.g., Coding, Debugging, Creative Writing).
- **Customizable LLM settings**: Provides recommended settings like temperature, verbosity, reasoning effort, and whether web access is required.
- **Zero-shot classification**: Uses a Hugging Face transformer model for zero-shot classification to predict categories without requiring training data.
- **Flask API**: A Flask-based API to receive POST requests and return categorized results and settings.

## API Endpoints

## `POST /classify`

Classifies a user prompt into relevant categories.

## Request:

{
  "prompt": "<user_text>"
}

### Example Use Case

1. Type a prompt such as "How do I fix this Python error?".
2. The model will classify it as "Coding" and "Debugging".
Recommended settings may include:
  temperature: 0.1
  reasoning_effort: "high"
  verbosity: "verbose"
  web: "optional"

## Technologies Used

- **Flask:** Python web framework for the API.
- **Hugging Face Transformers:** For zero-shot classification.
- **Streamlit:** For creating a simple frontend web app.

## Setup Instructions
- Prerequisites
Python 3.7 or higher
pip for installing dependencies

1. Clone the Repository
- git clone https://github.com/proshevav/Real-time-Prompt-Categorization-API.git
- cd Real-time-Prompt-Categorization-API

2. Create a Virtual Environment
- python -m venv .venv

3. Activate the Virtual Environment
- .venv\Scripts\activate

4. Install Dependencies
- pip install -r requirements.txt
  
5. Run the Flask API Server
- python app.py

The API will be available at http://127.0.0.1:5000.

## Frontend 

A basic Streamlit frontend is available for real-time prompt categorization.

To run the frontend:
1. Install Streamlit:
- pip install streamlit

2. Run the frontend:
- streamlit run frontend.py

This will start a web app where you can input prompts, and it will display the predicted categories and recommended settings in real time.
