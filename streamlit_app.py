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
#str_text = open("/workspaces/helpmeread/sample/sample1.txt").read()
#st.write(str_text)
