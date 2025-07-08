import streamlit as st
import google.generativeai as genai

# --- Configure your Gemini API key here ---
GENAI_API_KEY = "AIzaSyBYRT9pKGppgunzxpe91ylRDzsuWJbrNn4"
genai.configure(api_key=GENAI_API_KEY)

# --- Set up model ---
model = genai.GenerativeModel("gemini-2.0-flash")

# --- Streamlit UI ---
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="📢")
st.title("📢 LinkedIn Post Generator using Gemini")

# Inputs
topic = st.text_input("📝 Enter the topic for the LinkedIn post:")
tone = st.selectbox("🎯 Choose the tone of the post:", ["Professional", "Casual", "Motivational", "Inspirational", "Witty"])
word_count = st.slider("✍️ Desired number of words:", min_value=50, max_value=300, step=10, value=150)

# Button
if st.button("🚀 Generate Post"):
    if not topic:
        st.warning("⚠️ Please enter a topic.")
    else:
        with st.spinner("Generating with Gemini..."):
            prompt = (
                f"Write a LinkedIn post in a {tone.lower()} tone about '{topic}'. "
                f"The post should be approximately {word_count} words long."
            )
            try:
                response = model.generate_content(prompt)
                st.subheader("🧾 Generated LinkedIn Post")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Error: {e}")
