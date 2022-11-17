import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme ():
    hour = int(datetime.datetime.now().hour)

    if hour>2  and hour<12:
        speak("good morning")

    elif hour >= 18 and hour < 11 :
        speak("good ")

    elif hour >= 12 and hour < 18 :
        speak("good afternoon")
    else:
        speak("good evening")

    speak("i am jarvis sir , how may i help you")

def take_command():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}')
    except Exception as e:
        print('Say that again please...')
        return 'none'
    return query


#speak('ankit')
wishme()
while True:
    query = take_command().lower()

    if 'wikipedia' in query:
        speak("Searching wikipedia")
        query = query.replace('wikipedia','')
        results= wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif "open youtube" in query:
        webbrowser.open('www.youtube.com')

    elif "open google" in query:
        webbrowser.open('www.google.co.in')
    elif 'play music' in query:
        music_dir = 'D:\\Songs'
        songs= os.listdir(music_dir)
        #print(songs)
        os.startfile(os.path.join(music_dir, songs[4]))
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime('%H:%M')
        speak(f'sir, the time is {strTime}')
    elif "open vs code" in query:
        codepath ="C:\\Users\\akkib\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
    elif "open spotify" in query:
        spotpath ='C:\\Users\\akkib\\AppData\\Roaming\\Spotify\\Spotify.exe'
        os.startfile(spotpath)

    elif 'quit ' in query:
        break

    '''elif 'email to ankit' in query:
        try:
            speak('what should i say')
            content = take_command()
            to = 'ankitsankalp1997@gmail.com'
            sendEmail(to,content)
            speak('Email has been sent')
        except Exception as e:
            print(e)
            speak('Sorry there is some error')

    def '''