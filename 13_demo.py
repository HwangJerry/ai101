import streamlit as st
from dotenv import load_dotenv
from langchain_openai import OpenAI


load_dotenv()
llm = OpenAI(model="")


if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "message": "Hello, how can I help you?"}]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["message"])

if query := st.chat_input("Type your message"):
    st.session_state.messages.append({"role": "user", "message": query})
    st.chat_message("user").write(query)
    st.session_state.messages.append({"role": "assistant", "message": ""})
    st.chat_message("assistant").write("")
