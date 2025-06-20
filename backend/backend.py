from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend to communicate with backend

# Define root route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Chatbot backend is running!"})

# Define chatbot response function
def get_chatbot_response(user_input):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("user", "Question:{question}")
    ])
    
    llm = OllamaLLM(model="gemma:2b")
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    
    response = chain.invoke({"question": user_input})
    return response

# API endpoint for chatbot
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "").strip()
    
    if not user_input:
        return jsonify({"error": "Empty input"}), 400
    
    response = get_chatbot_response(user_input)
    return jsonify({"response": response})

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
