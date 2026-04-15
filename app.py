import streamlit as st

st.title("🚀 English Learning App")

st.write("Welcome to your personalized learning system!")

mode = st.selectbox("Choose mode", ["Vocabulary", "Speaking", "Pronunciation"])

if mode == "Vocabulary":
    st.write("📚 Vocabulary training coming soon...")

elif mode == "Speaking":
    st.write("🗣 Speaking practice coming soon...")

elif mode == "Pronunciation":
    st.write("🔊 Pronunciation training coming soon...")
