import pyttsx3 #text to specch converter
import wikipedia
import speech_recognition as sr
import datetime
import time
from random import *
import webbrowser
import pywhatkit
import os #open installed apps
import smtplib
#Text to speech converter
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)

#Speak function
def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour <12 :
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <18 :
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am your Sana, please tell me how may I help you?")

#Voice Recognizer
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said {query}")
    except  Exception as e :
        speak("Say again please..")
        return "None"
    return query
# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('mitraarijit99@gmail.com','madhabimitra')
#     server.sendmail('mitraarijit99@gmail.com',To,content)
#     server.close()
if __name__ == "__main__" :
    wishme()
    while True :
        query = takecommand().lower()
        #Logic for Executing tasks
        #Wikipedia Module
        if 'wikipedia' in query :
            speak('Searching Wikipedia..')
            query = query.replace("Wikipeda", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        #Webbrowser Module
        elif 'open youtube' in query :
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open("youtube.com")

        elif 'video call' in query :
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open("duo.google.com")

        #pywhatkit module
        # google search and youtube commad
        elif 'sana' in query:
            search = query.replace('sana', '')
            pywhatkit.search(search)
            try :
                results = wikipedia.summary(search, sentences=2)
                speak("According to wikipedia")
                speak(results)
            except Exception as e:
                e

        elif 'play' in query or 'youtube' in query:
            search = query.replace('play','')
            pywhatkit.playonyt(search)

        #Some System implementation
        elif 'music on device' in query :
            music_dir = 'C:\\Users\\DELL\\Music'
            songs = os.listdir(music_dir)
            song = songs[randint(0,57)]
            print(song)
            os.startfile(os.path.join(music_dir,song)) #randint take a random input

        elif 'time' in query :
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'date' in query :
            strdate = datetime.date.today()
            speak(f"Sir, today's date is {strdate}")

        elif 'vs code' in query:
            codepath = '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codepath)

        # elif 'email' in query:
        #     try :
        #         speak ("What should i say?")
        #         content = takecommand()
        #         To  = "suniketchakraborty86@gmail.com"
        #         sendEmail(To,content)
        #         speak("Email has been sent!")
        #     except Exception as e :
        #         speak("Email has been not send")

        elif 'eclipse' in query :
            os.startfile('C:\\Users\\DELL\\eclipse\\java-2020-062\\eclipse\\eclipse.exe')

        elif 'open google' in query :
            os.startfile('"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"')

        #Some Cool Questions
        elif 'thank you' in query or 'thanks' in query :
            List = ["It's my pleasure", "Your Welcome"]
            speak(List[randint(0,1)])

        elif 'arijit' in query :
            speak("He is my founder so I love him so much")

        elif 'who are you' in query :
            speak("I am Sana and arijit created me on January 2, 2021")

        elif 'love you' in query :
            speak("ofcourse I love you so much! thanks for using me so long")

        elif 'wish me' in query :
            time = int(datetime.datetime.now().hour)
            if time >= 6 and time < 12:
                speak("Good Morning Sir!")
            elif time >= 12 and time < 18:
                speak("Good Afternoon Sir")
            elif time >18 and time <20:
                speak("Good Evening Sir")
            else :
                speak("Good Night Sir")

        #Calculator
        elif 'square' in query :
            speak("Tell me the number")
            n1 = takecommand()
            try :
                speak(f"square is {int(n1)**2}")
            except Exception as e :
                speak("Try again! and Next time please speak a number!")
        # Break Statement
        elif 'bye' in query or 'exit' in query:
            ListforBye = ['take care! bye',
                          'see you later',
                          'good bye sir, I will miss you so much',
                          'bye',
                          'bye!',
                          'take care of you'
                         ]
            speak(ListforBye[randint(0,5)])
            break