
from ast import Try
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak ("I am cindrella sir. Please tell me how may i help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        return "None" 
    return query
    
def sendEmail(to, content):


   if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak ("According to wikipedia ")
            print(results)
            speak (results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strtrTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir , the time is {strtrTime}")

        elif 'open code' in query:
            codePath = "c:\\users\\Dell\\Appdata\\Programs\\Microsoft vs Code\\ Code.exe"
            os.startfile(codePath)
        
        elif 'email to rakhi' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "rakhisevi@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend rakhi ji. i m not able to snd this email")


             
                 





        
    
