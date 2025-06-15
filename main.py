import streamlit as st

ingest_page = st.Page("pages/ingest_page.py", title="Ingest")
chatbot_page = st.Page("pages/chatbot_page.py", title="Chatbot")

pg = st.navigation([
    ingest_page,
    chatbot_page
])

pg.run()
