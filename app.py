from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st

load_dotenv()

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

prompt_template = "Explain the term '{jargon_term}' in simple, easy-to-understand language suitable for a general audience, avoiding technical details and complex terminology."

def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text

st.title("Explain Jargon in Simple Way")

jargon_term = st.text_area("Enter the jargon you want to explain")
if st.button("Generate Explanation"):
    response = generate_content(prompt_template.format(jargon_term=jargon_term))
    st.write(response)
