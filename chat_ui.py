# chat_ui.py

import streamlit as st
import pygame

# Initialize pygame for sound
pygame.mixer.init()


# Function to play sound
def play_send_sound():
    send_sound = pygame.mixer.Sound('assets/send.mp3')
    send_sound.play()


# Function to display chatbox UI
def chat_ui():
    # Custom CSS for the UI styling
    st.markdown("""
        <style>
            .chat-box-container {
                position: relative;
                width: 100%;
                height: 80vh;
                padding-bottom: 70px; /* Give space for the input box */
                overflow-y: auto;
                background-color: #111;
                color: white;
                padding: 20px;
            }
            .input-box {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                padding: 10px;
                background-color: #222;
                display: flex;
                align-items: center;
                justify-content: space-between;
                box-shadow: 0px -3px 10px rgba(0, 0, 0, 0.5);
            }
            .input-box input {
                width: 80%;
                padding: 10px;
                border-radius: 25px;
                border: none;
                background-color: #333;
                color: white;
                font-size: 16px;
            }
            .mic-btn, .send-btn {
                background-color: #444;
                border-radius: 50%;
                width: 50px;
                height: 50px;
                display: flex;
                justify-content: center;
                align-items: center;
                border: none;
                cursor: pointer;
                color: white;
                font-size: 22px;
            }
            .send-btn {
                background-color: #5f5;
            }
        </style>
    """, unsafe_allow_html=True)

    # Chat box container (to show messages)
    st.markdown('<div class="chat-box-container" id="chat-box"></div>', unsafe_allow_html=True)

    # Input field with a mic button and send button
    with st.container():
        input_text = st.text_input("Type your message", key="message", placeholder="Type here...")

        # Mic button (if implemented)
        mic_button = st.button("🎤", key="mic", help="Start voice input", use_container_width=True, on_click=None)

        # Send button (circular arrow)
        send_button = st.button("➡️", key="send", help="Send message", use_container_width=True)

        # When user presses send
        if send_button:
            # Send message logic (play sound and show the message)
            play_send_sound()  # Play send sound
            st.write(f"You: {input_text}")  # Show user message
            input_text = ""  # Clear input box after sending the message
            # Here, you can add the logic for Nemesis' response as well.
