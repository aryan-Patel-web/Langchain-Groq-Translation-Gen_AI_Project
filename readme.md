Ollama-QA-Chatbot-Streamlit


An interactive Q&A chatbot built with Streamlit and Ollama open-source LLMs.  
Lets users query models like gemma, phi3, and mistral with custom temperature and token settings.  
Ideal for exploring open-source chat capabilities directly in your browser.



# Ollama-QA-Chatbot-Streamlit

An interactive Q&A chatbot built with Streamlit and Ollama open-source LLMs.  
Lets users query models like gemma, phi3, and mistral with custom temperature and token settings.  
Ideal for exploring open-source chat capabilities directly in your browser.

---

## 🚀 Features

✅ Streamlit web UI for easy interaction  
✅ Supports multiple Ollama LLMs (gemma, phi3, mistral)  
✅ Adjustable temperature and max tokens  
✅ Environment-configured LangChain tracing for debugging

---

## 🏗️ Project Structure


- **streamlit_app.py** → Main Streamlit app  
- **.env** → Holds API keys and environment variables  
- **requirements.txt** → Python dependencies  

---

## 📦 Requirements

- Python 3.9+
- Ollama and LangChain libraries
- OpenAI-compatible environment variables if tracing (optional)

Install dependencies:

```bash
pip install -r requirements.txt

langchain
langchain-openai
python-dotenv
langchain_community
langchain_core
streamlit


.env
LANGCHAIN_API_KEY=YOUR_LANGCHAIN_KEY
GROK_API_KEY=abc....

💻 How To Run

streamlit run streamlit_app.py

🔎 Example Usage

You: What is machine learning?
You: What is machine learning?
LLaMA: Machine learning is a branch of artificial intelligence focused on building systems that learn from data rather than being explicitly programmed...


👤 Author
Aryan Patel


🌟 Future Enhancements

Add support for more Ollama models

Implement conversation memory

Enable PDF uploads for context-based Q&A

Deploy to public hosting for live demos
