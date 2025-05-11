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
            background-image: url("https://i.pinimg.com/originals/5b/70/dc/5b70dce12b08ed89ab33a7437b44a377.jpg");
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
            font-family: 'Quicksand', sans-serif;
            position: relative;
            overflow: hidden;
        }}

      
       

# Add animated hearts and jar animation
heart_and_jar_animation = """


   st.markdown("""
    <style>
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

.heart {{
  color: #ffb6c1;
  font-size: 26px;
  animation: float 4s ease-in-out infinite;
  display: inline-block;
  margin: 0 6px;
}}

.jar {{
  width: 150px;
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

# Sound effect on jar pick
def add_jar_pick_sound():
    st.markdown(
        """
        <script>
        function playSound() {
          var audio = new Audio("https://www.fesliyanstudios.com/play-mp3/4386");
          audio.play();
        }
        </script>
        """,
        unsafe_allow_html=True
    )

# Add background, animations, and music
add_bg_from_url()
st.markdown(heart_and_jar_animation, unsafe_allow_html=True)
add_background_music()
add_jar_pick_sound()

# Page content
st.markdown("<h1 style='text-align: center; color: #FF69B4; font-family: Quicksand, sans-serif;'>Healing Jar for You</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: white; font-size: 18px;'>Choose how you're feeling, my love. A divine whisper awaits to bring peace to your heart.</p>", unsafe_allow_html=True)

# Emotions and Quotes (the dictionary block and rest remains as is)
# ... (quotes dictionary and rest of app continues here)


# 100 Quranic quotes categorized by emotion
quotes = {
    "Anger": [
        "And hasten to forgiveness from your Lord... (3:133)",
        "Indeed, Allah loves those who are constantly repentant. (2:222)",
        "And speak to people good [words]. (2:83)",
        "Who restrain anger and pardon people. (3:134)",
        "Repel evil with that which is better. (41:34)",
        "Do not be angry and Paradise will be yours. (Hadith)",
        "Indeed, those who fear Allah - when an impulse touches them from Satan, they remember [Him]. (7:201)",
        "And do not let the hatred of a people prevent you from being just. (5:8)",
        "Indeed, Allah commands justice and good conduct. (16:90)",
        "Be patient, for what they say. (20:130)",
        "Verily, with hardship comes ease. (94:6)",
        "Allah is with the patient. (8:46)",
        "Indeed, the mercy of Allah is near to the doers of good. (7:56)",
        "Take what is given freely, enjoin what is good, and turn away from the ignorant. (7:199)",
        "If someone wrongs you, be patient. (41:35)",
        "Do not insult those they invoke besides Allah. (6:108)",
        "Kind speech and forgiveness are better than charity. (2:263)",
        "Lower your wing to the believers. (15:88)",
        "Say kind words to people. (2:83)",
        "Forgive with grace. (15:85)"
    ],
    "Anxious": [
        "Indeed, my Lord is near and responsive. (11:61)",
        "Verily in the remembrance of Allah do hearts find rest. (13:28)",
        "Allah does not burden a soul beyond that it can bear. (2:286)",
        "So remember Me; I will remember you. (2:152)",
        "And rely upon Allah; and sufficient is Allah as Disposer of affairs. (33:3)",
        "Indeed, the help of Allah is near. (2:214)",
        "Unquestionably, by the remembrance of Allah hearts are assured. (13:28)",
        "Do not grieve; indeed Allah is with us. (9:40)",
        "Say, Nothing will happen to us except what Allah has decreed. (9:51)",
        "He knows what is within the hearts. (11:5)",
        "Indeed, He is Hearing and Seeing. (17:1)",
        "Your Lord has not forsaken you. (93:3)",
        "And your Lord is going to give you, and you will be satisfied. (93:5)",
        "Surely, the promise of Allah is true. (10:55)",
        "You may dislike something that is good for you. (2:216)",
        "Allah is the best of planners. (8:30)",
        "And Allah is the best of providers. (62:11)",
        "He created man and knows what whispers in his soul. (50:16)",
        "Put your trust in Allah. (3:159)",
        "He is with you wherever you are. (57:4)"
    ],
    "Stressed": [
        "Verily, with every difficulty there is relief. (94:6)",
        "So truly where there is hardship there is also ease. (94:5)",
        "And whoever puts their trust in Allah, then He will suffice him. (65:3)",
        "Indeed, your Lord is vast in forgiveness. (53:32)",
        "Allah is with the patient. (2:153)",
        "Do not lose hope in the mercy of Allah. (39:53)",
        "He gives strength to the weary. (94:6)",
        "And We have certainly made the Qur'an easy for remembrance. (54:17)",
        "So do not weaken and do not grieve. (3:139)",
        "Be not sad, surely Allah is with us. (9:40)",
        "Indeed, Allah is ever Knowing and Wise. (4:26)",
        "And your Lord is most forgiving. (18:58)",
        "Indeed, my protector is Allah. (7:196)",
        "He who relies upon Allah – then He is sufficient for him. (65:3)",
        "Indeed, Allah loves those who rely [upon Him]. (3:159)",
        "Truly, Allah is full of kindness. (16:7)",
        "Allah is with those who fear Him. (16:128)",
        "Your Lord is full of mercy. (6:147)",
        "Call upon Me; I will respond to you. (40:60)",
        "My success is only by Allah. (11:88)"
    ],
    "Low": [
        "And We have certainly honored the children of Adam. (17:70)",
        "Do not grieve; indeed, Allah is with us. (9:40)",
        "Indeed, with hardship comes ease. (94:6)",
        "So verily, with hardship, there is relief. (94:5)",
        "Your Lord has not forsaken you. (93:3)",
        "And Allah is the best of providers. (62:11)",
        "Indeed, Allah is with those who fear Him. (16:128)",
        "He loves those who do good. (2:195)",
        "We created man in the best stature. (95:4)",
        "Say, My Lord has commanded justice. (7:29)",
        "Allah is the ally of those who believe. (2:257)",
        "And it is He who gives life and causes death. (23:80)",
        "He created you and perfected your design. (82:7)",
        "Surely Allah is kind and merciful. (2:143)",
        "So never think Allah will fail in His promise. (14:47)",
        "Allah is never unjust to His servants. (22:10)",
        "Indeed, the mercy of Allah is near. (7:56)",
        "He is the most merciful of the merciful. (12:64)",
        "He is the Most Forgiving, the Most Loving. (85:14)",
        "And to Allah belong the best names. (7:180)"
    ],
    "Hopeless": [
        "Do not despair of the mercy of Allah. (39:53)",
        "Indeed, Allah forgives all sins. (39:53)",
        "He is Oft-Forgiving, Most Merciful. (39:53)",
        "Allah is with those who patiently persevere. (8:46)",
        "Verily, with hardship comes ease. (94:6)",
        "My Lord is with me; He will guide me. (26:62)",
        "Surely Allah is the best disposer of affairs. (3:173)",
        "And Allah is full of kindness to the people. (2:143)",
        "He is the best to protect and the best to help. (22:78)",
        "Indeed, the mercy of Allah is near. (7:56)",
        "Allah is sufficient for us. (3:173)",
        "Indeed, Allah is capable of everything. (2:20)",
        "Allah is with you wherever you may be. (57:4)",
        "To Allah belong the best names. (7:180)",
        "Whoever fears Allah, He will make a way. (65:2)",
        "He will provide from sources you never imagined. (65:3)",
        "And He is with you wherever you are. (57:4)",
        "Indeed, Allah is subtle with His servants. (42:19)",
        "Allah is ever Knowing and Wise. (4:26)",
        "Your Lord is never forgetful. (19:64)"
    ]
}



emotion = st.selectbox("What are you feeling right now?", list(quotes.keys()))

if st.button("Pick a Jar Slip"):
    chosen_quote = random.choice(quotes[emotion])
    st.markdown(f"""
        <div style='background-color:rgba(255,240,245,0.8); padding:20px; border-radius:20px; border: 2px solid #ffb6c1; box-shadow: 2px 2px 12px #ffb6c1;'>
            <p style='color:#800080; font-family: Georgia, serif; font-size: 18px; text-align: center;'><em>{chosen_quote}</em></p>
        </div>
    """, unsafe_allow_html=True)
