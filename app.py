# Install and import required packages
import streamlit as st
from gtts import gTTS
import pyttsx3

#text - to - speech using gtts
def text_to_speech_gtts(text):
    tts = gTTS(text)
    tts.save("output.mp3")
    st.audio("output.mp3", format="audio/mp3")

#text - to - speech using pyttsx3
def text_to_speech_pyttsx3(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()
    st.audio("output.mp3", format="audio/mp3")

def main():
    st.title("Text to Speech App")
    text = st.text_area("Enter the text you want to convert to speech:")
    engine_choice = st.radio("Choose TTS Engine:", ("gtts", "pyttsx3"))

    if st.button("Convert to Speech"):
        if engine_choice == "gtts":
            text_to_speech_gtts(text)
        elif engine_choice == "pyttsx3":
            text_to_speech_pyttsx3(text)

if __name__ == "__main__":
    main()
