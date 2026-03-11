import streamlit as st
import requests

st.title("Autonomous AI Research Agent")

query = st.text_input("Enter research topic")

if st.button("Research"):

    response = requests.post(
        "http://127.0.0.1:8000/research",
        params={"query": query}
    )

    result = response.json()

    st.write(result["response"])