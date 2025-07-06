# 🤖 Jarvis - AI Voice Assistant (Python Project)

Jarvis is a personal voice assistant built with Python that can respond to voice commands, search the web, play YouTube videos, answer questions using Gemini AI, send WhatsApp messages, and perform system actions like shutdown/restart. Wake it up by simply saying "Jarvis".

---

## 🎯 Features

- 🎙️ **Voice Activation** with wake word "Jarvis"
- 💬 **Gemini AI integration** for intelligent answers
- 🔍 **Google Search** via voice
- 📺 **Play YouTube Videos**
- 📱 **Send WhatsApp Messages**
- 🕑 **Tells time and date**
- 🖥️ **Shutdown / Restart System with voice confirmation**
- 🎧 **Speech recognition using Google Speech API**
- 🧠 Uses `dotenv` to securely manage API keys

---

## 🧠 Tech Stack

- Python
- `speech_recognition` for capturing voice
- `pyttsx3` for text-to-speech
- `googleapiclient` for YouTube search
- `google.generativeai` for Gemini AI
- `pywhatkit` for WhatsApp automation
- `dotenv` for managing API keys securely

---

## 🛠 Setup Instructions

1. Clone the repository  
   ```bash
   git clone https://github.com/ramdevpyla64/Ai-voice-assistant.git
   cd Ai-voice-assistant
2. Create a `.env` file with your API keys:

3. Install required libraries  
```bash
pip install -r requirements.txt

4. Run the assistant
```bash
python jarvis1.py
