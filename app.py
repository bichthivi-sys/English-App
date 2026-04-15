import streamlit as st
import pandas as pd
from datetime import datetime
import os

DATA_FILE = "app_data.csv"

st.set_page_config(page_title="English Learning App", layout="centered")

st.title("🚀 AI English Learning System")

# ===================== LOAD DATA =====================
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame({
        "word": ["tariff", "regression", "model"],
        "meaning": ["thuế", "hồi quy", "mô hình"],
        "ipa": ["/ˈtærɪf/", "/rɪˈɡreʃən/", "/ˈmɒdəl/"],
        "topic": ["Economics", "Data", "General"],
        "question": ["What is tariff?", "Explain regression", "What is a model?"],
        "answer": ["A tax on imports", "A statistical method", "A simplified representation"],
        "correct": [0, 0, 0],
        "wrong": [0, 0, 0],
        "last_seen": ["", "", ""]
    })

# Priority logic
df["priority"] = df["wrong"] - df["correct"]
df = df.sort_values("priority", ascending=False)

row = df.iloc[0]

# ===================== MODE =====================
mode = st.selectbox("Choose Mode", ["Vocabulary", "Speaking", "Pronunciation"])

# ===================== VOCAB =====================
if mode == "Vocabulary":
    st.subheader(f"📘 {row['word']}")

    if st.button("Show Meaning"):
        st.success(row["meaning"])

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ I know"):
            df.loc[row.name, "correct"] += 1
            df.loc[row.name, "last_seen"] = datetime.today()

    with col2:
        if st.button("❌ I don't know"):
            df.loc[row.name, "wrong"] += 1
            df.loc[row.name, "last_seen"] = datetime.today()

# ===================== SPEAKING =====================
elif mode == "Speaking":
    st.subheader(f"🗣 Topic: {row['topic']}")
    st.write(f"Question: {row['question']}")

    user_answer = st.text_area("Your answer")

    if st.button("Show Sample Answer"):
        st.info(row["answer"])

# ===================== PRONUNCIATION =====================
elif mode == "Pronunciation":
    st.subheader(f"🔊 {row['word']}")
    st.write(f"IPA: {row['ipa']}")

# ===================== SAVE =====================
df.to_csv(DATA_FILE, index=False)
