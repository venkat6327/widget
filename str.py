import streamlit as st
import streamlit.components.v1 as components

# Load your widget's HTML (with embedded CSS + JS if possible)
with open("chat_widget.html", "r", encoding="utf-8") as f:
    widget_code = f.read()

# Render inside Streamlit
components.html(widget_code, height=600, scrolling=True)
