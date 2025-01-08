import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

user_input = input("Something")

response = model.generate_content(f"Say a dad joke using {user_input}")
print(response.text)