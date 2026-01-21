import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="Chatbot 🤖")
st.title("🤖 OpenAI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Type your message")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    reply = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
