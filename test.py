import speech_recognition as sr
from ollama_api import get_response

def listen_and_respond():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")

            # Get AI response
            ai_response = get_response(user_input)
            print(f"Nemesis AI: {ai_response}")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
        except sr.RequestError:
            print("Could not request results, please check your internet connection.")

if __name__ == "__main__":
    while True:
        listen_and_respond()
