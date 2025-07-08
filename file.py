import streamlit as st
import google.generativeai as genai

# --- Gemini API Key ---
API_KEY = "AIzaSyBYRT9pKGppgunzxpe91ylRDzsuWJbrNn4"  # Replace with your actual Gemini API key
genai.configure(api_key=API_KEY)

# --- Model Name ---
MODEL_NAME = "gemini-2.0-flash"
model = genai.GenerativeModel(MODEL_NAME)

# --- Page Configuration ---
st.set_page_config(page_title="LinkedIn Post Generator", layout="centered")

# --- Custom CSS for colorful background ---
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #FF2DD1, #c2e9fb);
    }
    .stApp {
        background: linear-gradient(135deg, #f6d365, #fda085);
        padding: 2rem;
        border-radius: 10px;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: black;
    }
    .stButton button {
        background-color: Black;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- App UI ---
st.title("📢 LinkedIn Post Generator")

topic = st.text_input("📝 Enter the topic for the LinkedIn post:")
tone = st.selectbox("🎯 Choose the tone:", ["Professional", "Casual", "Motivational", "Inspirational", "Witty"])
word_count = st.slider("✍️ Number of words:", 50, 300, 150, 10)

if st.button("🚀 Generate"):
    if not topic:
        st.warning("⚠️ Please enter a topic.")
    else:
        with st.spinner("Generating using Gemini..."):
            prompt = f"Write a LinkedIn post in a {tone.lower()} tone about '{topic}' in about {word_count} words."
            try:
                response = model.generate_content(prompt)
                st.subheader("🧾 Generated LinkedIn Post")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Error: {e}")
