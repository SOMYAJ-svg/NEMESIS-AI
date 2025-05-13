import ollama


# Conversation history
chat_history = []

def get_response(user_input):
    global chat_history

    # Add user message to history
    chat_history.append({"role": "user", "content": user_input})

    try:
        # Get response from AI
        response = ollama.chat(
            model="mistral:7b",
            messages=chat_history
        )

        # Extract AI response
        ai_message = response['message']['content']

        # Append AI response to history
        chat_history.append({"role": "assistant", "content": ai_message})

        return ai_message

    except Exception as e:
        return f"Error: {str(e)}"

