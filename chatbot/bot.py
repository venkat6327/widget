import streamlit as st
import time

# Page config
st.set_page_config(page_title="Chatbot UI", page_icon="💬", layout="wide")

# Init history
if "history" not in st.session_state:
    st.session_state.history = [{"role": "bot", "text": "Hi! I'm Sam. How can I help you?"}]

# Fake reply generator (replace with real model/API call)
def generate_reply(user_input):
    time.sleep(0.5)  # simulate delay
    return f"You said: {user_input}"

# --- Custom CSS for floating chatbox ---
st.markdown("""
<style>
    .chatbox-container {
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 350px;
        max-height: 500px;
        display: flex;
        flex-direction: column;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        background: white;
        overflow: hidden;
        font-family: "Nunito", sans-serif;
        z-index: 9999;
    }
    .chatbox-header {
        background: linear-gradient(93.12deg, #581B98 0.52%, #9C1DE7 100%);
        padding: 12px;
        color: white;
        font-weight: bold;
        text-align: center;
    }
    .chatbox-messages {
        flex: 1;
        padding: 10px;
        overflow-y: auto;
        background: #f8f9fa;
    }
    .msg {
        margin: 8px 0;
        padding: 8px 12px;
        border-radius: 15px;
        max-width: 70%;
    }
    .msg-user {
        background: #581B98;
        color: white;
        margin-left: auto;
        border-bottom-right-radius: 5px;
    }
    .msg-bot {
        background: #E0E0E0;
        color: black;
        margin-right: auto;
        border-bottom-left-radius: 5px;
    }
    .chatbox-input {
        display: flex;
        border-top: 1px solid #ddd;
    }
    .chatbox-input input {
        flex: 1;
        border: none;
        padding: 10px;
        outline: none;
    }
    .chatbox-input button {
        background: #9C1DE7;
        color: white;
        border: none;
        padding: 0 20px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)

# --- Floating Chatbox ---
with st.container():
    st.markdown('<div class="chatbox-container">', unsafe_allow_html=True)

    # Header
    st.markdown('<div class="chatbox-header">💬 Chat Support</div>', unsafe_allow_html=True)

    # Messages
    st.markdown('<div class="chatbox-messages">', unsafe_allow_html=True)
    for msg in st.session_state.history:
        role_class = "msg-user" if msg["role"] == "user" else "msg-bot"
        st.markdown(f'<div class="msg {role_class}">{msg["text"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Input
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("Message", "", label_visibility="collapsed")
        submitted = st.form_submit_button("Send")
        if submitted and user_input:
            st.session_state.history.append({"role": "user", "text": user_input})
            reply = generate_reply(user_input)
            st.session_state.history.append({"role": "bot", "text": reply})
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
