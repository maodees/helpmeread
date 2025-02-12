import streamlit as st
from openai import OpenAI
import os

st.title("🎈 My new app")
st.write(
    "Let's start building a! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

st.write(os.getcwd())
str_text = open("/mount/src/helpmeread/sample/sample1.txt").read()
st.write(str_text)

prompt = "Summarise the content with focus on the intent and action required"

client = OpenAI(api_key=openai_api_key)
st.session_state.messages.append({"role": "user", "content": prompt})
#st.chat_message("user").write(prompt)
response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
msg = str_text
st.session_state.messages.append({"role": "assistant", "content": msg})
st.write(msg)
