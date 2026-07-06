import pdfplumber
from gtts import gTTS
import os

pages_lst = []

print("Extracting text...")
with pdfplumber.open("AI for everyone book.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            pages_lst.append(text)

full_text = " ".join(pages_lst)


print("Converting to audio...")
tts = gTTS(text=full_text, lang='en')
tts.save("output.mp3")

print("Done! Playing audio...")
os.startfile("output.mp3")
