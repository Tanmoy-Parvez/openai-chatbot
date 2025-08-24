import os
import time
import threading
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

thinking_flag = True

def show_thinking():
    dots = ""
    while thinking_flag:
        print(f"\r🤖 Bot is thinking{dots}   ", end="", flush=True)
        dots = dots + "." if len(dots) < 3 else ""
        time.sleep(0.5)

def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        if hasattr(e, "http_status") and e.http_status == 429:
            return "⚠️ API quota exceeded. Please try again later."
        return f"⚠️ Error: {str(e)}"

if __name__ == "__main__":
    print("\n🤖 Chatbot is ready! (type 'quit' to exit)\n")
    
    while True:
        user_input = input("🧑 You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("\n🤖 Bot: Goodbye! 👋\n")
            break

        # Start thinking animation in background
        thinking_flag = True
        t = threading.Thread(target=show_thinking)
        t.start()

        # Get reply from API
        reply = chat_with_gpt(user_input)

        # Stop thinking animation
        thinking_flag = False
        t.join()

        # Clear line and print reply
        print(f"\r🤖 Bot: {reply}\n")
