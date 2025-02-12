import streamlit as st
from openai import OpenAI

st.title("🎈 My new app")
st.write(
    "Let's start building a! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

str_text = open("sample\sample1.txt").read()
st.write(str_text)
