import langchain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import llamacpp
import streamlit as st

prompt = ChatPromptTemplate.from_messages(
    
    [
        ("system", "You are a helpful assistant. Please respond to the questions"),
        ("user", "Question:{question}")
    ]
)

st.title('Interactive ChatBot (UI)') 
input_text = st.text_input("You can ask any question.")

llm = llamacpp(model = "llama3.2")

chain = prompt|llm

if input_text:
    st.write(chain.invoke({"question":input_text}))
