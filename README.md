# Gem Bot – A Lightweight LLM Chatbot Backend
Gem Bot is a simple and modular Flask-based chatbot backend that leverages Ollama’s Gemma:2B language model and LangChain to deliver natural and helpful responses. It exposes a REST API, making it easy to integrate with any frontend interface.

## Features

Powered by Ollama + Gemma 2B local LLM

LangChain integration with structured prompt and output parsing

CORS-enabled Flask backend for cross-origin access

API-ready for chat-based frontend integration

Environment-based secure configuration

## Getting Started

Clone the repository and navigate to the project folder.

Set up a Python virtual environment.

Install dependencies using pip install -r requirements.txt.

Create a .env file and add the following keys:

OPENAI_API_KEY=your_openai_key

LANGCHAIN_API_KEY=your_langchain_key

LANGCHAIN_PROJECT=GemBot

LANGCHAIN_TRACING_V2=true

Run the server using python app.py.

Your backend will be live at: http://localhost:5000

## API Endpoints

GET /
Returns: { "message": "Chatbot backend is running!" }

POST /chat
Payload: { "message": "Your question here" }
Returns: { "response": "Chatbot's reply" }

## License
MIT License — Free to use and modify for personal or commercial projects.

