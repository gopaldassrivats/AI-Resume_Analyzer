import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
print("API Key Found:", api_key is not None)

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-2.5-flash")

def analyze(resume, jd):

    prompt = f"""
    Resume:
    {resume}

    Job Description:
    {jd}

    Give:
    1. ATS Score
    2. Missing Skills
    3. Suggestions
    """

    response = model.generate_content(prompt)

    return response.text