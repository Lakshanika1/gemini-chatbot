import os
from google.genai import Client
client = Client(api_key=os.getenv("GOOGLE_API_KEY"))
print("🤖 Gemini Chatbot is running...")
print("Type 'exit' to stop.\n")
chat_history = []
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye 👋")
        break
    chat_history.append({
        "role": "user",
        "parts": [{"text": user_input}]
    })
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=chat_history[-6:]   # limit history
        )
        bot_reply = response.text
        print("Chatbot:", bot_reply)
        chat_history.append({
            "role": "model",
            "parts": [{"text": bot_reply}]
        })
    except Exception as e:
        print("Error:", e)
        break