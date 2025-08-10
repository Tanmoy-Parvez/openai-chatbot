import openai
from dotenv import load_dotenv
import os
load_dotenv()  # Reads .env file and loads variables into environment


openai.api_key=os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    res = openai.ChatCompletion.create()
        model="gpt-5",
        messages=[{
            "role":"user", "content":prompt
        }]
    return res.choices[0].message.content.strip()

