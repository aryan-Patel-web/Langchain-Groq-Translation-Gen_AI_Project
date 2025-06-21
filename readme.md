# 🌐 LangChain Groq Translation API

This is a lightweight translation API built with **FastAPI**, **LangChain**, and **Groq's Gemma2-9b-it** model. The server exposes a `/chain` endpoint that accepts input text and the target language, and returns the translated result.

## 🚀 Features

- 🔁 Translates user text into a target language using LLM
- ⚡ Powered by Groq's high-speed inference
- 🧩 Modular LangChain Runnables with LangServe FastAPI routing

---

## 🛠️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/langchain-groq-translation-api.git
   cd langchain-groq-translation-api


Create virtual environment and install dependencies


python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt


Set up environment variables

Create a .env file in the root directory with your Groq API key:


GROK_API_KEY=your_groq_api_key_here

▶️ Running the API

uvicorn main:app --reload
Once running, access your API at http://127.0.0.1:8000/chain


📬 Example Request
POST /chain/invoke
Request Body:

{
  "input": {
    "text": "How are you?",
    "language": "French"
  }
}

Response:

{
  "output": "Comment ça va ?"
}


🧩 Stack
LangChain

LangServe

Groq + Gemma2-9b-it

FastAPI

# Langchain-Groq-Translation-Gen_AI_Project
