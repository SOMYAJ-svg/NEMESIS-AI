# reaction_engine.py
import random

reaction_map = {
    "success": ["🎉", "✅", "🙌", "😎"],
    "error": ["😅", "❌", "😓", "💀"],
    "love": ["❤️", "🥺", "💖", "😘"],
    "motivation": ["🔥", "💪", "🚀", "✨"],
    "greeting": ["👋", "😊", "💫", "🙋‍♀️"],
    "sad": ["😢", "💔", "🥺", "😭"],
    "slay": ["😈", "👑", "💅", "🖤"]
}

def get_reaction(message: str) -> str:
    message = message.lower()
    for keyword, reactions in reaction_map.items():
        if keyword in message:
            return random.choice(reactions)
    return ""
