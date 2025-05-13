import tkinter as tk
from ollama_api import get_response

def send_message():
    user_input = entry.get()
    if user_input:
        chat_history.insert(tk.END, f"You: {user_input}\n", "user")
        entry.delete(0, tk.END)

        ai_response = get_response(user_input)
        chat_history.insert(tk.END, f"Nemesis AI: {ai_response}\n", "bot")

# GUI Setup
root = tk.Tk()
root.title("Nemesis AI")

chat_history = tk.Text(root, wrap=tk.WORD, height=20, width=50)
chat_history.pack()

entry = tk.Entry(root, width=40)
entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()
