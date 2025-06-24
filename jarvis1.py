from googlesearch import search
import speech_recognition as sr
import webbrowser
import pyttsx3
from googleapiclient.discovery import build
import re
import time
import google.generativeai as genai
from datetime import datetime
import pywhatkit as pwk
import os
from dotenv import load_dotenv
load_dotenv()
r=sr.Recognizer()

api_key2 = os.getenv("YOUTUBE_API_KEY")
genai_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=f"{genai_api_key}")
model=genai.GenerativeModel("gemini-2.0-flash")
chat=model.start_chat()
engine = pyttsx3.init()
engine.setProperty('rate', 150)
count=0
def ai(command):
    response=chat.send_message(command)
    return response.text
def get_youtube_link(query):
    try:
        youtube = build("youtube", "v3", developerKey=f"{api_key2}")
        request = youtube.search().list(
            part="snippet",
            q=query,
            maxResults=1,
            type="video"
        )
        response = request.execute()
        video_id = response['items'][0]['id']['videoId']
        return f"https://www.youtube.com/watch?v={video_id}"
    except Exception as e:
        print(f"YouTube API Error: {e}")
        return None
def speak(text):
    engine.say(text)
    engine.runAndWait()
def whatsapp():
    speak("Please enter the phone number including country code:")
    phone_number = input("Phone number: ")
    speak("Listening for message...")
    for _ in range(3): 
        try:
            with sr.Microphone() as source:
                r.energy_threshold = 100  
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=10, phrase_time_limit=30)
                message = r.recognize_google(audio)
                print(f"Message: {message}")
                break
        except Exception as e:
            print(f"Error recognizing speech: {e}")
            speak("Sorry, I didn't catch that. Try again.")
    else:
        speak("Failed to get message after multiple tries.")
        return
    pwk.sendwhatmsg_instantly(phone_number, message)

def command(word):
    if "open" in word:
        query = word.replace("open", "").strip()
        print("You said:", query)

        try:
            for result in search(query, num_results=1):
                print("Top link:", result)
                webbrowser.open(result)
                speak(f"Opening {query}")
                break
        except Exception as e:
            print(f"Search error: {e}")
            speak("I couldn't find anything to open.")
    elif "shutdown system" in word or "shut down system" in word:
        print("shutting down the system in 30 secs if you want to stop say 'abort shutdown'")
        speak("shutting down the system in 30 secs if you want to stop say 'abort shutdown'")
        try:
            with sr.Microphone() as source:
                r.energy_threshold = 100 
                audio=r.listen(source,timeout=2, phrase_time_limit=5)
                print("recognizing....")
                word2=r.recognize_google(audio)
                print(word2)
            if word2.lower()=="abort shutdown":
                return
        except:
            time.sleep(1)
            os.system("shutdown /s /t 1")
            return
    elif "restart system" in word or "reboot" in word:
        print("restarting the system now in 30 secs if you want to stop say 'abort retstart'")
        speak("restarting the system now in 30 secs if you want to stop say 'abort retstart'")
        try:
            with sr.Microphone() as source:
                r.energy_threshold = 100 
                audio=r.listen(source,timeout=2, phrase_time_limit=5)
                print("recognizing....")
                word2=r.recognize_google(audio)
                print(word2)
            if word2.lower()=="abort shutdown":
                return
        except:
            time.sleep(1)
            os.system("shutdown /r /t 1")
            return

    elif "what is your name" in word:

        speak("My name is Jarvis")

    elif "who are you" in word:

        speak("I am just a bunch of code, but I'm functioning properly")

    elif word.startswith("play"):
        yt_query = word.replace("play","")
        link = get_youtube_link(yt_query)
        if link:
            webbrowser.open(link)
            speak(f"Playing {yt_query}")
        else:
            speak("Sorry, I couldn't find that song.")
    elif "send" in word and "whatsapp" in word:
        whatsapp()
    else:
        content=ai(word)
        print("ai:",content)
        clean_content = re.sub(r'[^\x00-\x7F]+', ' ', content)
        speak(clean_content)
def reading():
    while True:
        try:
            print("start speaking.....")
            with sr.Microphone() as source:
                r.energy_threshold = 100  
                audio=r.listen(source,timeout=40, phrase_time_limit=10000)
                print("recognizing....")
                word1=r.recognize_google(audio)
                print(word1)
            if word1=="exit":
                  speak("signing off!jarvis")
                  time.sleep(0.5)
                  engine.stop()
                  break
            elif word1=="":
                 speak("can't able to hear you")
            else:
                 command(word1.lower())  
        except:
             pass       
if __name__=="__main__":
    speak("jarvis initialized")
    while True:
        try:
            with sr.Microphone() as source:
                r.energy_threshold = 100
                audio=r.listen(source,timeout=10, phrase_time_limit=120)
                word=r.recognize_google(audio)
                print(word)
                word=word.lower()
            if "jarvis" in word:
                if word.startswith("jarvis"):
                    if word.lower()=="jarvis":
                        speak("yes")
                        reading()
                    else:
                        word1=word.replace("jarvis ","").strip()
                        print(word1)
                        if word1.lower()=="exit":
                            break
                        command(word1.lower())
                        reading()
            else:
                pass           
        except:
            pass