import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Check if the error has an http_status attribute for rate limit errors
        if hasattr(e, "http_status") and e.http_status == 429:
            return "Sorry, the API quota has been exceeded. Please try again later."
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    print("Start chatting with the bot (type 'quit', 'exit' or 'bye' to stop):")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        reply = chat_with_gpt(user_input)
        print("Chatbot:", reply)
