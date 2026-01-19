import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import os

st.title("Multilingual Audio to Text System")

uploaded_file = st.file_uploader("Upload WAV audio file", type=["wav"])

language = st.selectbox(
    "Select Language",
    ["en-IN", "hi-IN", "te-IN", "ta-IN"]
)

if uploaded_file is not None:
    with open("temp.wav", "wb") as f:
        f.write(uploaded_file.read())

    recognizer = sr.Recognizer()
    with sr.AudioFile("temp.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language=language)
        st.success("Transcription Successful")
        st.write(text)
    except:
        st.error("Could not recognize speech")
