import streamlit as st
import random
import base64

# Set page config FIRST
st.set_page_config(page_title="Healing Jar", layout="centered")

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


# Lily animation simulation using emojis
st.markdown("<h3 style='text-align: center;'>🌸 Tap the button to bloom lilies 🌸</h3>", unsafe_allow_html=True)
if st.button("Bloom More Lilies 💐"):
    for _ in range(10):
        line = "".join(["🌸" if random.random() > 0.2 else " " for _ in range(20)])
        st.markdown(f"<div style='text-align:center;font-size:25px;'>{line}</div>", unsafe_allow_html=True)
    # Page content
st.markdown("<h1 style='text-align: center; color: #FF69B4; font-family: Quicksand, sans-serif;'>Healing Jar for You</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: white; font-size: 18px;'>Choose how you're feeling, my love. A divine whisper awaits to bring peace to your heart.</p>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #FF69B4; font-family: Quicksand, sans-serif;'>Healing Jar for You</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: white; font-size: 18px;'>Choose how you're feeling, my love. A divine whisper awaits to bring peace to your heart.</p>", unsafe_allow_html=True)

# Emotions and Quotes
emotions = ["Stressed", "Anxious", "Angry", "Low", "Overthinking"]
choice = st.selectbox("How are you feeling today?", emotions)

quotes = {
    "Stressed": ["Indeed, with hardship comes ease. – Quran 94:6"] * 20,
    "Anxious": ["Verily, in the remembrance of Allah do hearts find rest. – Quran 13:28"] * 20,
    "Angry": ["And those who restrain anger and who pardon the people – Allah loves the doers of good. – Quran 3:134"] * 20,
    "Low": ["Do not despair of the mercy of Allah. – Quran 39:53"] * 20,
    "Overthinking": ["Put your trust in Allah; surely, Allah loves those who trust. – Quran 3:159"] * 20
}

if st.button("Pick a Healing Slip 💌"):
    selected_quote = random.choice(quotes[choice])
    st.markdown(f"<div style='padding:20px; background-color:##F8C8DC; border-radius:20px; text-align:center; font-size:20px;'><em>\"{selected_quote}\"</em></div>", unsafe_allow_html=True)



