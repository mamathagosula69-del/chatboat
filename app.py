import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Check API key
if not api_key:
    st.error("GEMINI_API_KEY is not found in the .env file.")
    st.stop()

# Create Gemini client
client = genai.Client(api_key=api_key)

# Page settings
st.set_page_config(
    page_title="Gemini AI Chatbot",
    layout="centered"
)

# Title
st.title("🤖 Gemini AI Chatbot")
st.write("Ask Gemini anything!")

# Prompt input
prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Artificial Intelligence"
)

# Generate response
if st.button("Generate Response"):

    if prompt.strip():

        with st.spinner("Gemini is thinking..."):

            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                st.success("Response generated!")
                st.write(response.text)

            except Exception as e:
                st.error("Something went wrong:")
                st.exception(e)

    else:
        st.warning("Please enter a prompt.")
