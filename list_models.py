import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('MODEL_API_KEY')
genai.configure(api_key=api_key)

print("Available models:")
print("-" * 50)

for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"Model: {model.name}")
        print(f"Display Name: {model.display_name}")
        print(f"Supported methods: {model.supported_generation_methods}")
        print("-" * 50)
