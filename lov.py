import streamlit as st
import time
import random

st.set_page_config(page_title="Women's Day Wish", layout="centered")

# Custom background with pastel gradient
page_bg = """
<style>
body {
    background: linear-gradient(to right, #fbc2eb, #a6c1ee);
    font-family: 'Arial', sans-serif;
    color: #333;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: #e91e63;'>🌸 Happy Women's Day, My Love! 🌸</h1>", unsafe_allow_html=True)

# Lily animation simulation using emojis
lily_area = st.empty()
for _ in range(30):
    lily_line = "".join(["🌸" if random.random() > 0.2 else " " for _ in range(20)])
    lily_area.markdown(f"<div style='text-align:center;font-size:25px;'>{lily_line}</div>", unsafe_allow_html=True)
    time.sleep(0.15)


