from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
# LangSmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant. Respond to the user queries"),
        ("user", "Question:{question}")
    ]
)

# Streamlit Framework
st.title('LangChain Demo With Gemma API')
input_text=st.text_input("Search the topic you want to")

# Ollama Gemma LLM 
llm=Ollama(model="gemma")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))