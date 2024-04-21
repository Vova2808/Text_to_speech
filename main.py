# pip install gTTS
from gtts import gTTS
import os


file = str(input("Введите текст для озвучки: "))

speech = gTTS(text=file, lang='en', slow=False)
speech.save("voice.mp3")
os.system("voice.mp3")
