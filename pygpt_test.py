import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("API_KEY")

prompt = "Say this is a test"

response = openai.Completion.create(
    model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=7)
print(response)
