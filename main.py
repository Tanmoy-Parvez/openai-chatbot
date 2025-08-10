import openai

openai.api_key=""

def chat_with_gpt(prompt):
    res = openai.ChatCompletion.create()
        model="gpt-5"
        messages=[{
            "role":"user", "content":prompt
        }]
    return res.choices[0].message.content.strip()