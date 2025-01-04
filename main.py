import google.generativeai as genai
import os

geminiAPI = os.environ['geminiapi']

genai.configure(api_key=geminiAPI)
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("Explain how AI works")
print(response.text)