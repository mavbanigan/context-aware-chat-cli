# Terminal Chat Assistant

A conversational virtual assistant that runs in your terminal, powered by OpenAI's GPT-4o-mini model. 
It maintains full conversation history, so the model remembers previous messages and relevant context.

## Features
- Persistent conversation memory within separate sessions
- Graceful error handling for network issues
- Secure API key management via environment variables

## Setup

1. Clone the repository
   git clone https://github.com/yourusername/terminal-chat-assistant.git

2. Install dependencies
   pip install -r requirements.txt

3. Create a .env file in the project root and add your OpenAI API key
   OPENAI_API_KEY=your-key-here

4. Run the chatbot
   python chat.py

## Usage
- Type any message and press Enter to chat
- Type 'quit' to exit

## Tech Stack
- Python
- OpenAI API (GPT-4o-mini)
- python-dotenv

## Author
Maverick Banigan - github.com/mavbanigan
