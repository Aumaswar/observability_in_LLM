from openai import OpenAI
from dotenv import load_dotenv
import os

# Langfuse imports
from langfuse import observe
from langfuse.openai import openai

# Load env
load_dotenv()

# Configure Groq client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("AI Chatbot Started (type 'exit' to quit)\n")


@observe()
def chat():

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chat ended.")
            break

        try:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            )

            print("AI:", response.choices[0].message.content)
            print()

        except Exception as e:
            print("Error:", e)


chat()