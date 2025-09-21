# app.py
import streamlit as st
import streamlit.components.v1 as components
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import time
import os

# ---------------- Flask backend ----------------
app = Flask(__name__)
CORS(app)  # allow cross-origin for local dev

@app.route("/chat", methods=["POST"])
def chat_api():
    data = request.get_json(force=True)
    user_message = data.get("message", "")
    # === PLACE YOUR AI / BUSINESS LOGIC HERE ===
    # Example: simple echo reply. Replace with model call / DB / API.
    reply = f"You said: {user_message}"
    return jsonify({"response": reply})

def run_flask():
    # use_reloader=False to avoid Flask spawning child process (important when run inside thread)
    app.run(host="127.0.0.1", port=5001, debug=False, use_reloader=False)

# start Flask in background thread
flask_thread = threading.Thread(target=run_flask, daemon=True)
flask_thread.start()

# small wait to help Flask start before front-end tries to call it
time.sleep(0.2)

# ---------------- Streamlit frontend ----------------
st.set_page_config(page_title="Streamlit + Chat Widget", layout="wide")
st.title("ds")

# Load your merged HTML
with open("chat_widget.html", "r", encoding="utf-8") as f:
    widget_code = f.read()

# Render the widget in Streamlit
components.html(widget_code, height=700, scrolling=True)
