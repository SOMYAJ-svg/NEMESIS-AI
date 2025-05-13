# import pygame
#
# def play_send_sound():
#     try:
#         if not pygame.mixer.get_init():
#             pygame.mixer.init()
#         pygame.mixer.music.load("assets/message-send.mp3")
#         pygame.mixer.music.play()
#     except Exception as e:
#         print("🔊 Sound Error:", e)
#

from pathlib import Path
from shutil import copyfile

# Absolute path to where the file was uploaded via Streamlit earlier
source = "/mnt/data/message-send.mp3"

# Destination
assets_path = Path("/Users/somya/PycharmProjects/NEMESIS/assets")
assets_path.mkdir(parents=True, exist_ok=True)
target = assets_path / "message-send.mp3"

# Copy
copyfile(source, target)
print("✅ Sound file copied to assets folder.")
