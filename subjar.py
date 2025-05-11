import streamlit as st
import random
import base64

# Set page config FIRST
st.set_page_config(page_title="Healing Jar", layout="centered")

# Background image function (cute aesthetic)
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap');

        .stApp {{
            background-image: url("https://i.pinimg.com/originals/bd/1f/21/bd1f218a2d166963509d3f932e4c13bb.jpg");
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
            font-family: 'Quicksand', sans-serif;
            overflow-x: hidden;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Add animated hearts and jar animation
heart_and_jar_animation = """
<style>
@keyframes float {{
  0% {{ transform: translateY(0px); }}
  50% {{ transform: translateY(-15px); }}
  100% {{ transform: translateY(0px); }}
}}

.heart {{
  color: #ffb6c1;
  font-size: 26px;
  animation: float 4s ease-in-out infinite;
  display: inline-block;
  margin: 0 6px;
}}

.jar {{
  width: 180px;
  margin: 0 auto;
  display: block;
  animation: float 5s ease-in-out infinite;
  border-radius: 20px;
  box-shadow: 0px 0px 20px pink;
}}
</style>
<div style='text-align:center;'>
  <span class='heart'>💖</span>
  <span class='heart'>💗</span>
  <span class='heart'>💞</span>
</div>
<br>
<img src='https://i.pinimg.com/originals/8a/80/6f/8a806f3a0473484ddcd10d6a9987813d.gif' class='jar'>
"""

# Soft romantic music embed
def add_background_music():
    st.markdown(
        """
        <audio autoplay loop>
            <source src="https://www.bensound.com/bensound-music/bensound-love.mp3" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

# Add background, animations, and music
add_bg_from_url()
st.markdown(heart_and_jar_animation, unsafe_allow_html=True)
add_background_music()

# Page content
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
    st.markdown(f"<div style='padding:20px; background-color:#fff0f5; border-radius:20px; text-align:center; font-size:20px;'><em>\"{selected_quote}\"</em></div>", unsafe_allow_html=True)
