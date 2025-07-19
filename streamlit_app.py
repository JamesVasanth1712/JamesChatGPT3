import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="JamesChatGPT")
st.title("🤖 JamesChatGPT (Free LLM Version)")
st.write("Ask anything — I'm here to help you!")

# Load model once
if "chatbot" not in st.session_state:
    st.session_state.chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:", placeholder="Type your question and press Enter")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        response = st.session_state.chatbot(user_input, max_length=100, do_sample=True, top_k=50, top_p=0.95)
        reply = response[0]['generated_text']
        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.success("JamesGPT: " + reply)

st.subheader("Chat History")
for msg in st.session_state.messages:
    role = "You" if msg["role"] == "user" else "JamesGPT"
    st.markdown(f"**{role}:** {msg['content']}")
