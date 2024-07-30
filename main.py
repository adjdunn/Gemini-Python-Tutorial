from pathlib import Path
from openai import OpenAI
import pygame
import time
import os


def text_to_speech(text):
    
    client = OpenAI()

    speech_file_path = Path(__file__).parent / "speech2.mp3"
    os.remove(speech_file_path)

    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="nova",
        input=text,
    ) as response:
        response.stream_to_file(speech_file_path)

    pygame.mixer.init()
    pygame.mixer.music.load(speech_file_path)
    pygame.mixer.music.play()

    # Keep the program running long enough for the audio to play
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    pygame.mixer.quit()

    
    
