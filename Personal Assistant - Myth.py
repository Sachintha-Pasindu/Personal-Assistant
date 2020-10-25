import speech_recognition as sr
import pyttsx3
import PyPDF2
import re
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    statement = input("Command : ")
    try:
        print(f"user said:{statement}\n")

    except Exception as e:
        speak("Pardon me, please say that again")
        return "None"
    return statement

print("Loading your AI personal assistant The Myth")
speak("Loading your personal assistant The Myth")
wishMe()


if __name__=='__main__':


        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()


if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant The Bot is shutting down,Good bye')
            print('your personal assistant The Bot is shutting down,Good bye')
            


if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

elif 'news' in statement:
            news = webbrowser.open_new_tab("https://www.news.lk/news")
            speak('Here are some latest news from the news.lk ,Happy reading')
            time.sleep(6)
                                           
elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

elif 'ask' in statement:
            speak('Connecting to wolframalpha knowledgebase...')
            print("connected to wolframalpha...")
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            app_id="you app id"
            client = wolframalpha.Client('your app id')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
                

elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am The Bot version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')

elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Myth")
            print("I was built by Myth")


elif "weather" in statement:
            api_key="Your open weather api key"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

			
time.sleep(3)


























