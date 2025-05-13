# streamlit_ui.py

from ollama import chat  # Make sure you have `ollama` Python SDK installed

def generate_response(user_input):
    try:
        response = chat(
            model='mistral:7b',  # You're using mistral 7B via ollama
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        return response['message']['content']
    except Exception as e:
        return f"❌ Error: {str(e)}"

import streamlit as st
from streamlit.components.v1 import html

st.markdown("""
    <style>
        .chat-container {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #1e1e1e;
            padding: 12px 16px;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 100;
            border-top: 1px solid #333;
        }

        .chat-input-box {
            background-color: #2a2a2a;
            border-radius: 24px;
            padding: 10px 16px;
            display: flex;
            align-items: center;
            width: 100%;
            max-width: 800px;
        }

        .chat-input-box input {
            background: transparent;
            border: none;
            outline: none;
            color: #fff;
            font-size: 16px;
            flex: 1;
        }

        .icon-btn {
            width: 32px;
            height: 32px;
            background: #fff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-left: 10px;
            cursor: pointer;
        }

        .icon-btn:hover {
            background: #ccc;
        }

        .icon-btn i {
            color: #000;
        }
    </style>

    <div class="chat-container">
        <div class="chat-input-box">
            <input type="text" placeholder="Ask anything..." id="user-input" />
            <div class="icon-btn" onclick="startMic()">
                <i class="fa fa-microphone"></i>
            </div>
            <div class="icon-btn" onclick="toggleSpeaker()">
                <i class="fa fa-volume-up"></i>
            </div>
        </div>
    </div>

    <script>
        function startMic() {
            console.log("Mic button clicked");
            // TODO: trigger mic function
        }

        function toggleSpeaker() {
            console.log("Speaker button clicked");
            // TODO: toggle voice response
        }
    </script>
""", unsafe_allow_html=True)

