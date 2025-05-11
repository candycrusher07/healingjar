import streamlit as st
import random
import base64

# Set page config FIRST
st.set_page_config(page_title="Healing Jar", layout="centered")

import streamlit as st

# Inject custom CSS with your background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: #c490fc;
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #fffafc;
    }}
   
 h2 {{
        text-align: center;
        color: #b86f91;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""
<style>
div.stButton > button {
    color: #b86f91 !important;          /* Text color */
    background-color: #ffe0f0 !important; /* Background */
    border-radius: 12px;
    border: 1px solid #b86f91;
    font-weight: bold;
    font-size: 18px;
    transition: 0.3s ease;
}
div.stButton > button:hover {
    background-color: #fcd5eb !important;
    color: #8b3a62 !important;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)


# Initialize session state
if "u_count" not in st.session_state:
    st.session_state.u_count = 1
if "show_love" not in st.session_state:
    st.session_state.show_love = False

# Title or Heading
st.markdown(
    "<h2 style='text-align: center; color: #b86f91;'>🌸 Tap the button to bloom lilies 🌸</h2>",
    unsafe_allow_html=True
)

# Button to show "I LOVE YOU" made of lilies
if st.button("Tap to Bloom"):
    st.session_state.show_love = True
    st.session_state.u_count = 1  # reset on new tap

# Button to bloom more 'u's
if st.button("Bloom More Lilies 💐"):
    if st.session_state.show_love:
        st.session_state.u_count += 1

# Display the text made of lilies
if st.session_state.show_love:
    love_message = f"I LOVE YOU{'U' * (st.session_state.u_count - 1)}"
    st.markdown("<div style='text-align:center;font-size:32px;'>", unsafe_allow_html=True)
    for char in love_message:
        if char == " ":
            st.markdown("&nbsp;&nbsp;", unsafe_allow_html=True)
        else:
            st.markdown(f"<span style='color:#ff66b2;'>{'🌸' * 1} {char} {'🌸' * 1}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    # Page content
st.markdown("<h1 style='text-align: center; color: #FF69B4; font-family: Quicksand, sans-serif;'>Healing Jar for You</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: white; font-size: 18px;'>Choose how you're feeling, my love. A divine whisper awaits to bring peace to your heart.</p>", unsafe_allow_html=True)

# Emotions and Quotes
emotions = ["Stressed", "Anxious", "Angry", "Low", "Overthinking", "BreakUp"]


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
    ],
    "BreakUp": [
        "Tell sorry to guddu and go to sleep",
        "Psych ain't leaving you girl",
        "Sharam Karro"
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
