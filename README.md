 Gem Bot – A Lightweight LLM Chatbot Backend
Gem Bot is a simple and modular Flask-based chatbot backend that leverages Ollama’s Gemma:2B language model and LangChain to deliver natural and helpful responses. It exposes a REST API, making it easy to integrate with any frontend interface.

✨ Features
Powered by Ollama + Gemma 2B local LLM

LangChain integration with structured prompt and output parsing

CORS-enabled Flask backend for cross-origin access

API-ready for chat-based frontend integration

Environment-based secure configuration

🚀 Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/gem-bot.git
cd gem-bot
2. Set Up Virtual Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file:

bash
Copy
Edit
touch .env
And add the following keys:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_key
LANGCHAIN_API_KEY=your_langchain_key
LANGCHAIN_PROJECT=GemBot
LANGCHAIN_TRACING_V2=true
5. Run the Server
bash
Copy
Edit
python app.py
Your backend will be live at http://localhost:5000

🧠 API Endpoints
GET /

Returns: Chatbot backend is running!

POST /chat

Payload: { "message": "Your question here" }

Returns: { "response": "Chatbot's reply" }

🗂️ Project Structure
bash
Copy
Edit
gem-bot/
├── app.py               # Main Flask app
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables
└── README.md            # Project documentation
📄 License
MIT License — Free to use and modify for personal or commercial projects.
