import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import os
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,0,4)
        
    try:
        print("Understanding....")
        query = r.recognize_google(audio,language= 'en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()
            
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("ok Sir, You can call me anytime")
                    break
                    
                elif "hello" in query:
                    speak("Hello sir, kesa hai bhai tu ?")
                
                elif "friends" in query:
                    speak("Friends are good, but himanshu is bhen ka louda and suraj is the papa of himanshu and pratik is the dada of both ")
                    
                elif "i am fine" in query:
                    speak("that's great, sir")
                    
                elif "thanks" in query:
                    speak("You are welcome, sir")
                    
                elif "my father" in query:
                    speak("your father is Antaryami Satpathy")
                    
                elif "my mother" in query:
                    speak("Your mother is Sobha rani Satpathy")
                    
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                    
                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                    
                elif "Weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeaWE").text
                    speak(f"current{search} is {temp}")
                    
                elif "shutdown the system" in query:
                    speak("Shutting down the system")
                    os.system("shutdown /s /t 1")
                    
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                    
                elif "finally you sleep now" in query:
                    speak("Going to sleep sir, Thank you")
                    exit()  