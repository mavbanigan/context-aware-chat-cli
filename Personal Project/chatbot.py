# This imports the libraries for the API 
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
# This is the variable that safely holds my openAI key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# This is the main function that runs the chatbot
def chat():
    # This structures the console for the user's input
    print("The chatbot is ready! Type 'quit' to stop the chatbot.\n")

    # This stores the conversation history so the GPT bot remembers context from past conversations.
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    # This is the actual part of the function that runs as long as the user hasn't typed
    # 'quit' into the terminal.
    while True:
        user_input = input("You: ")
        # breaks the loop if the user types 'quit'
        if user_input.lower() == "quit":
            break

        # Add the user's message to the history
        messages.append({"role": "user", "content": user_input})

        #Everything is wrapped in a try/except block, so if there's a network issue, the program doesn't completely crash.
        try:
            # Sends the full conversation history to the API so the model has context for its responses.
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )
            #Add the bot's response to the history
            messages.append({"role": "assistant", "content": response.choices[0].message.content})
            # Print the bot's reply to the terminal
            print("Bot:", response.choices[0].message.content)
        except Exception as e:
            print("Error:", e)
# This runs the chat() function if the user is in the main terminal
if __name__ == "__main__":
    chat()
