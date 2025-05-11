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
            background-image: url("https://www.freecodecamp.org/news/content/images/size/w2000/2021/06/w-qjCHPZbeXCQ-unsplash.jpg");
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
            font-family: 'Quicksand', sans-serif;
            overflow-x: hidden;
        }}

        .sparkles {{
            position: absolute;
            width: 100%;
            height: 100%;
            background: url('https://i.gifer.com/4tyu.gif') repeat;
            background-size: cover;
            z-index: -1;
        }}
        </style>
        <div class='sparkles'></div>
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
  width: 200px;
  margin: 0 auto;
  display: block;
  animation: float 5s ease-in-out infinite;
  border-radius: 20px;
  box-shadow: 0px 0px 20px pink;
}}
lily_area = st.empty()
for _ in range(30):
    lily_line = "".join(["🌸" if random.random() > 0.2 else " " for _ in range(20)])
    lily_area.markdown(f"<div style='text-align:center;font-size:25px;'>{lily_line}</div>", unsafe_allow_html=True)
    time.sleep(0.15)

</style>
<div style='text-align:center;'>
  <span class='heart'>💖</span>
  <span class='heart'>💗</span>
  <span class='heart'>💞</span>
</div>
<br>
<img src='https://i.gifer.com/4tyu.gif' class='jar'>
"""

# Soft romantic music embed
def add_background_music():
    st.markdown(
        """
        <iframe src="https://www.youtube.com/embed/ZsTCRYF1kYg?autoplay=1&loop=1&playlist=ZsTCRYF1kYg&controls=0" width="0" height="0" frameborder="0" allow="autoplay"></iframe>
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
    st.markdown(f"<div style='padding:20px; background-color:##F8C8DC; border-radius:20px; text-align:center; font-size:20px;'><em>\"{selected_quote}\"</em></div>", unsafe_allow_html=True)
