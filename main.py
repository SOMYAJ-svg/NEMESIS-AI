import streamlit as st
from ollama_api import get_response
import pyttsx3
import speech_recognition as sr
import threading
import os
import json

import streamlit.components.v1 as components


MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(messages):
    with open(MEMORY_FILE, "w") as f:
        json.dump(messages, f)

def reset_memory():
    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)
    return []

# ---- Theme Selection ----
theme_choice = st.selectbox("🎨 Choose Theme", ["Classic Dark Neon", "Cyber Rose Sexy", "Matrix Code"])
# ---- Animation Toggle ----




# ---- Apply Selected Theme ----
if theme_choice == "Classic Dark Neon":
    css_style = """
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f0f0f, #1e1e1e) !important;
        color: #ffffff !important;
        font-family: 'Fira Code', monospace;
    }
    h1, h2, h3, h4 {
        color: #00ffee !important;
        font-weight: bold;
        text-shadow: 0 0 8px #00ffee;
    }
    input, textarea, select {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: 1px solid #00ffee !important;
        border-radius: 6px;
        padding: 8px;
    }
    button {
        background-color: #00ffee !important;
        color: #000000 !important;
        font-weight: bold;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        border: none;
        box-shadow: 0 0 10px #00ffee;
        transition: 0.3s ease;
    }
    button:hover {
        background-color: #00ccdd !important;
        box-shadow: 0 0 20px #00ffee;
    }
    label, .stTextInput > label, .stSelectbox > label {
        color: #bbbbbb !important;
        font-weight: bold;
        font-size: 0.9rem;
    }
    .stChatMessage, .css-1y0tads {
        background-color: rgba(255,255,255,0.05) !important;
        border: 1px solid #00ffee33;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 8px;
        color: #eeeeee;
    }
    ::-webkit-scrollbar-thumb {
        background: #00ffee;
    }
    </style>
    """

elif theme_choice == "Matrix Code":
    css_style = """
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #000000, #001100) !important;
        color: #00ff00 !important;
        font-family: 'Courier New', monospace;
    }
    h1, h2, h3, h4 {
        color: #00ff00 !important;
        text-shadow: 0 0 10px #00ff00;
    }
    input, textarea, select {
        background-color: #002200 !important;
        color: #00ff00 !important;
        border: 1px solid #00ff00 !important;
        border-radius: 4px;
        padding: 8px;
    }
    button {
        background-color: #00ff00 !important;
        color: #000000 !important;
        font-weight: bold;
        border-radius: 4px;
        padding: 0.5rem 1rem;
        border: none;
        box-shadow: 0 0 10px #00ff00;
    }
    button:hover {
        background-color: #00cc00 !important;
        box-shadow: 0 0 20px #00ff00;
    }
    ::-webkit-scrollbar-thumb {
        background: #00ff00;
        border-radius: 10px;
    }
    </style>
    """

else:  # Cyber Rose Sexy
    css_style = """
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a0d1f, #0e0512) !important;
        color: #fdfdfd !important;
        font-family: 'Fira Code', monospace;
    }
    h1, h2, h3, h4 {
        color: #ff66cc !important;
        font-weight: bold;
        text-shadow: 0 0 8px #ff66cc;
    }
    input, textarea, select {
        background-color: #2c1a2e !important;
        color: #ffffff !important;
        border: 1px solid #ff66cc !important;
        border-radius: 6px;
        padding: 8px;
    }
    button {
        background-color: #ff66cc !important;
        color: #000000 !important;
        font-weight: bold;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        border: none;
        box-shadow: 0 0 10px #ff66cc;
        transition: 0.3s ease;
    }
    button:hover {
        background-color: #ff33aa !important;
        box-shadow: 0 0 20px #ff66cc;
    }
    label, .stTextInput > label, .stSelectbox > label {
        color: #ffb6e6 !important;
        font-weight: bold;
        font-size: 0.9rem;
    }
    .stChatMessage, .css-1y0tads {
        background-color: rgba(255,255,255,0.08) !important;
        border: 1px solid #ff66cc33;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 8px;
        color: #fff0f5;
    }
    ::-webkit-scrollbar-thumb {
        background: #ff66cc;
    }
    </style>
    """

# ---- Apply CSS ----
st.markdown(css_style, unsafe_allow_html=True)
# ---- Optional Neon Particle Animation ----
if st.checkbox("✨ Enable Floating Animation", value=True):
    st.markdown("""
    <style>
    .floating-dot {
        width: 10px;
        height: 10px;
        background-color: #00ff00;
        border-radius: 50%;
        position: fixed;
        animation: floatAnim 8s infinite ease-in-out;
        z-index: 9999;
    }

    @keyframes floatAnim {
        0% { transform: translateY(0px) translateX(0px); opacity: 0.3; }
        25% { transform: translateY(-50vh) translateX(10vw); opacity: 0.6; }
        50% { transform: translateY(-100vh) translateX(-10vw); opacity: 1; }
        75% { transform: translateY(-50vh) translateX(5vw); opacity: 0.6; }
        100% { transform: translateY(0px) translateX(0px); opacity: 0.3; }
    }
    </style>
    <div class="floating-dot" style="left:10%; top:90%;"></div>
    <div class="floating-dot" style="left:30%; top:95%; animation-delay: 2s;"></div>
    <div class="floating-dot" style="left:70%; top:92%; animation-delay: 4s;"></div>
    <div class="floating-dot" style="left:50%; top:98%; animation-delay: 6s;"></div>
    """, unsafe_allow_html=True)


# ---- Title ----
st.title("🤖🦾 Nemesis AI")

# ---- TTS (Text to Speech) ----
def speak(text):
    def run():
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)
        engine.setProperty('volume', 1.0)
        engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')  # Adjust for macOS
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run).start()

# ---- Initial Startup ----
if "started" not in st.session_state:
    speak("Hello, I am Nemesis. Your personal AI assistant.")
    st.session_state.started = True
    st.session_state.voice_reply = False

# ---- Voice Response Toggle ----
st.session_state.voice_reply = st.checkbox("🔊 Want voice response?", value=st.session_state.get("voice_reply", False))

# ---- Chat History (Custom Bubbles) ----
if "messages" not in st.session_state:
    st.session_state.messages = load_memory()



chat_bubble_css = """
<style>
.message-container {
    display: flex;
    align-items: flex-start;
    margin-bottom: 16px;
}
.user-container {
    justify-content: flex-end;
}
.bot-container {
    justify-content: flex-start;
}
.user-avatar, .bot-avatar {
    font-size: 26px;
    margin: 0 10px;
}
.user-msg, .bot-msg {
    max-width: 70%;
    padding: 12px 16px;
    border-radius: 16px;
    font-family: 'Fira Code', monospace;
    font-size: 15px;
    line-height: 1.5;
}
.user-msg {
    background: rgba(0, 255, 255, 0.1);
    border: 1px solid #00ffee80;
    color: #ccfaff;
    text-align: right;
}
.bot-msg {
    background: rgba(255, 102, 204, 0.1);
    border: 1px solid #ff66cc80;
    color: #ffd9ec;
    text-align: left;
}

</style>
"""
st.markdown(chat_bubble_css, unsafe_allow_html=True)

# ---- Render All Chat at Once ----
def render_chat():
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="message-container user-container">
                <div class="user-msg">{msg["content"]}</div>
                <div class="user-avatar">🧬</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="message-container bot-container">
                <div class="bot-avatar">🤖</div>
                <div class="bot-msg">{msg["content"]}</div>
            </div>
            """, unsafe_allow_html=True)

# Show chat history first
render_chat()


# --- Floating Circular Reset Button (Top-Left) ---
reset_button_css = """
<style>
#floating-reset {
    position: fixed;
    top: 60px;
    left: 20px;
    z-index: 9999;
    background-color: #ff4b4b;
    color: white;
    border: none;
    border-radius: 50%;
    width: 45px;
    height: 45px;
    font-size: 20px;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    transition: all 0.3s ease-in-out;
}
#floating-reset:hover {
    background-color: #e63946;
    transform: scale(1.1);
}
</style>
<button id="floating-reset" onclick="window.dispatchEvent(new Event('resetMemory'))">🧹</button>
<script>
    const doc = window.parent.document;
    window.addEventListener('resetMemory', function () {
        const streamlitEvents = new Event("streamlit:rerunScript");
        doc.dispatchEvent(streamlitEvents);
        fetch('/_stcore/stream', {
            method: 'POST',
            body: JSON.stringify({"clearMemory": true}),
            headers: {'Content-Type': 'application/json'}
        });
    });
</script>
"""
st.markdown(reset_button_css, unsafe_allow_html=True)

# Python-side logic to clear memory
if st.query_params.get("clearMemory"):
    st.session_state.messages = reset_memory()
    st.experimental_set_query_params()  # clear params after
    st.success("Memory cleared!")
    st.rerun()


# ---- Voice Input Button ----

if st.button("🎙️"):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        st.info("🎧 Listening...")
        audio_data = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio_data)
        st.success(f"🗣️ You said: {text}")

        if "bye" in text.lower():
            st.info("Nemesis: Goodbye!")
            speak("Goodbye! See you soon.")
            st.stop()

        st.session_state.messages.append({"role": "user", "content": text})
        response = get_response(text)
        st.session_state.messages.append({"role": "assistant", "content": response})

        if st.session_state.voice_reply:
            speak(response)

        st.rerun()  # Refresh chat cleanly

    except sr.UnknownValueError:
        st.warning("😕 Couldn't understand you, please try again!")

# ---- Text Input Fallback ----
user_input = st.text_input("💬 Type your message:")

if st.button("Send") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    save_memory(st.session_state.messages)

    if st.session_state.voice_reply:
        speak(response)


    # Refresh chat cleanly
    st.rerun()


