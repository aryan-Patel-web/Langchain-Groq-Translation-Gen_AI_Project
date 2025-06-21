import streamlit as st
import openai
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder

from langchain_community.llms import Ollama

import os
from dotenv import load_dotenv
load_dotenv()

# langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"] = "true"

os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot WITH Ollama"

# prompt template define
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant . please response to the user queries"),
        ("user","Question:{question}")
    ]

)

## intract with llm
def generate_response(question , engine , temperature , max_tokens):
    # create chat openai

    llm=Ollama(model=engine)
    output_parser= StrOutputParser()

    # chain = how intraction is going to happen
    chain=prompt | llm | output_parser

    # generating
    answer = chain.invoke({'question':question})
    return answer



# streamlit 
st.title("Q&A Chatbot with OpenAI")

st.write("This is a simple Q&A chatbot using Open-Source LLaMA model.")

st.sidebar.title("Setting")


## dropdown

engine = st.sidebar.selectbox("Select an Ollama MOdel", ["gemma:2b", "phi3","mistral"])

temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)

# temperature=st.slider.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)

# interface

st.write("Go ahead and ask me a question!")

user_input = st.text_input("You:")

if user_input:
    answer =generate_response(user_input ,engine, temperature , max_tokens)
    st.write("LLaMA - :", answer)

else:
    st.write("Please enter a question to get an answer.")