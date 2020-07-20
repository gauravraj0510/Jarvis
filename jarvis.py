import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import random

webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    
    speak('I am Jarvis. Please tell me how can I help you!')

def takeCommand():
    # function to take microphone input from users and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        print('Say that again please!...')
        return "None" 
     
    return query



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.get('chrome').open('youtube.com')

        elif 'google' in query:
            webbrowser.get('chrome').open('google.com')
        
        elif 'instagram' in query:
            webbrowser.get('chrome').open('instagram.com')

        elif 'github' in query:
            webbrowser.get('chrome').open('github.com')

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Gaurav Raj\\Music\\Green Day'
            songs = os.listdir(music_dir)
            rand = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[rand]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is: {strTime}\n")




