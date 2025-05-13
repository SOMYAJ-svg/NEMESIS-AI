import streamlit as st
import speech_recognition as sr

# Function to handle voice input
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Say something...")
        audio = recognizer.listen(source)

        try:
            st.write("Recognizing...")
            text = recognizer.recognize_google(audio)
            st.write("You said: " + text)
        except sr.UnknownValueError:
            st.write("Sorry, I could not understand the audio")
        except sr.RequestError as e:
            st.write(f"Error with the speech recognition service: {e}")

# Streamlit UI
def app():
    st.title("Voice Input Streamlit App")

    if st.button("Start Listening"):
        recognize_speech()

if __name__ == "__main__":
    app()
