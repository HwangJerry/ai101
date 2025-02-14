from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5,
)

if "messages" not in st.session_state:
    st.session_state.messages = []

# 기존 채팅 기록 렌더링
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력 처리
if prompt := st.chat_input("메시지를 입력하세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    lc_messages = [HumanMessage(content=msg["content"]) if msg["role"] == "user" else AIMessage(content=msg["content"]) for msg in st.session_state.messages]

    with st.chat_message("assistant"):
        response_stream = llm.stream(lc_messages)

        full_response = st.write_stream(
            chunk.content for chunk in response_stream
        )

        st.session_state.messages.append({"role": "assistant", "content": full_response})