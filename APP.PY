import streamlit as st

st.title("🤖 FAQ Chatbot")

faqs = {
    "What is AI?": "AI stands for Artificial Intelligence.",
    "What is Python?": "Python is a programming language.",
    "What is Machine Learning?": "Machine Learning is a branch of AI.",
    "What is ChatGPT?": "ChatGPT is an AI chatbot.",
    "What is GitHub?": "GitHub is used to store code."
}

question = st.selectbox("Select a Question", list(faqs.keys()))

if st.button("Get Answer"):
    st.success(faqs[question])
    