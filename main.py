import pyttsx3 # pip instll pyttsx3
import speech_recognition as sr # pip install speechRecognition
import datetime # to get time so that jarvis can tell us
import pyaudio # necessary for pttsx3 and other modules 
import wikipedia # pip install wikipedia
import webbrowser # we can tell jarvis to open any website like facebook with it
import os # very important to make jarvis open necessary files for us
import random # so that it can play random songs and it also has other uses
import cv2 # for opening camera and face reconigazion 
import requests # to make a request to a website
import numpy # for implementing many more functions s
from requests import get # so that it can request any text of a website 
import pywhatkit as kit # it can send whatsapp message automatticaly
import sys # for implementing sys.exit() command
import pyjokes # so that our jarvis can tell jokes to us
import pyautogui # with this we can automate many things
from plyer import notification # with this our jarvis can send us notification 
import PyPDF2 # pip install PyPDF2
import json # to get raw data in JSON format 
from pytube import YouTube # to download youtube videos
import smtplib # to send emails 
import wolframalpha # computer intellegence
import pyautogui as auto # to make automation in gui's
import time # to implement time.sleep() 
import psutil # to get cpu and battery status
# import pystory 
from phonenumbers import * # to track a phone number 
import winsound # to play sounds for alarms and timers
import pyzbar.pyzbar as pyzbar # to scan qr code
import winshell # to implemet empty recycle bin
from tkinter import *
from englisttohindi.englisttohindi import EngtoHindi
import datef 


# setup
Bot_name = "Jarvis"
wolframalpha_api_key = "P7YJ38-7E47GPRTA5"
news_apiKey = "3f673f6e650547158c861f6d4807dac1"
weather_api = "f56744f45cb3faa1cd924b08724639e4"

# expressions
doing_well = [
    "That's My pleasure sir", 
    "Thank you sir",
    "Thank you very much sir",
    "It's good to know that you are enjoying with me",
] 
great = [ 
    "Really sir, i am i doing well?",
    "Thank you very much sir",
    "So will you give me a holiday for that?",
]
unhappy = [
    "I am not happy for that sir", 
    "I am not in the mood to talk" 
    "please me alone sir, i don't to want to talk now"
]
Play_romantic_song_array = [
"Aaj Se Teri", 

 "Tere Mere", 

 "Main Tere Kabil Hoon",  

 "Enna Sona",  

 "Humsafar",  

 "Lambiyaan Si Judaiyan",  

 "Ban Ja Rani",  

 "Nazm Nazm", 
]



try:
    app = wolframalpha.Client(wolframalpha_api_key)  
except Exception:
    print("Some features will not work due to no internet connection") 




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate') 
# print(rate) 
# print(voices[1].id)
engine.setProperty('voice', voices[0].id) 




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening")

    strTime = datetime.datetime.now().strftime("%H:%M:%S")  
    ts = time.strftime("%A, %d %B")  

    speak(f"sir, I am {Bot_name}, it's {strTime}  How may i Help You")     
  

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Listening...")
        r.energy_threshold =3500 
        r.pause_threshold = 1
        audio = r.listen(source) 

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n") 

    except Exception as e:
        # print(e)
        print("Say That again please") 
        return "Jarvis" 
    return query 



def pdf_reader():
    book = open('hack.pdf', 'rb') 
    pdfReader = PyPDF2.PdfFileReader(book) 
    pages = pdfReader.numPages
    speak(f"The total number of pages in this book are {pages}")
    speak("Sir please enter the page number, i have to read") 
    pg = int(input("Please enter the page number :")) 
    page = pdfReader.getPage(pg) 
    text = page.extractText() 
    speak(text) 

def news():
    pass 
    main_url = f"http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apikey={news_apiKey}" 

    main_page = requests.get(main_url).json() 
    # print(main_page) 
    articles = main_page["articles"]
    # print(articles) 
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh"]  
    for ar in articles:
        head.append(ar["title"])
        pass 
    for i in range (len(day)):
        engine.setProperty("rate", 170) 
        print(f"today's {day[i]} news is: {head[i]}") 
        speak(f"today's {day[i]} news is: {head[i]}") 
        pass 
        engine.setProperty("rate", 190) 

def CurrentWeather():
    speak("For which city sir") 
    weather_place = TakeCommand().lower() 
    Weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={weather_place}&appid={weather_api}" 

    api_link = requests.get(weather_api) 
    Weather_data = api_link.json() 

    if Weather_data['cod'] == '404':
        print(f"Invalid City: {weather_place}, Please check your city name".format(weather_place))  
    else:
        city_temprature = (Weather_data['main']['temp'] -273.15) 
        weather_desc = Weather_data['weather'][0]['description']
        humidity = Weather_data['main']['humidity'] 
        wind_speed = weather_data['wind']['speed'] 

        print(f"Current temprature is: {temprature} degree celcius")  
        print("Current Weather description is :",weather_desc)
        print("Current Humidity is :",humidity)
        print("Current wind speed :",wind_speed) 
        speak(f"Current temprature is: {temprature} degree celcius") 
        speak("Current Weather description is :",weather_desc) 
        speak("Current Humidity is :",humidity)
        speak("Current wind speed :",wind_speed) 



def scan():
    i = 0
    cap = cv2.VideoCapture(0) 
    while i<4:
        _,frame = cap.read() 
        decoded = pyzbar.decode(frame) 
        for obj in decoded:
            print(obj.data) 
            i = i+1

        cv2.imshow("Jarvis QR code scanner",frame)  
        cv2.waitKey(10) 
        cv2.destroyAllWindows 

# def Play_romantic_song(): 

        

    
if __name__ == "__main__":
    WishMe()
    # OnlineClasses()
    while True:
        query = TakeCommand().lower()

        # logic for executing the query

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to wikipedia")
            print(results)
            engine.setProperty('rate',170)  
            speak(results)  
            engine.setProperty('rate', 200) 

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            speak("Opening YouTube")

        elif 'open github' in query:
            webbrowser.get('chrome %s').open_new_tab('http://www.github.com') 
            speak("Opening Github")
        
        elif 'open google' in query:
            webbrowser.open('google.com')
            speak("Opening Google")
        
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
            speak("Opening stackoverflow")

        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            # print(songs) 
            rndom_song = random.choice(songs)
            speak("Playing Music") 
            os.startfile(os.path.join(music_dir, rndom_song)) 
            

        elif 'the time' in query: 
            now = datetime.datetime.now() 
            print(f"The current time is {now}")
            speak(f"The current time is {now}") 


        elif 'open code' in query: 
            Codepath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(Codepath)
            speak("opening Visual Studio Code") 
        
        elif 'open notepad' in query:
            Notepad_path = "C:\\Windows\\System32\\notepad.exe"
            speak("Opening Notepad")
            os.startfile(Notepad_path)

        elif 'translate english to hindi' in query: 
            speak("Sir, tell the sentence which you want me to translate hindi to english")
            Sentence = TakeCommand().lower()
            res = EngtoHindi(Sentence) 
            print(res.convert)
            speak(res.convert)

        elif 'write a note' in query or 'write note' in query:
            speak("What should i write sir?")
            note = TakeCommand()
            file = open('data.txt', 'w')
            speak("Sir should i include date and time?")
            snfm = TakeCommand().lower()
            if 'yes' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")  
                speak("Okay i have implemented the date and time along with the note")
                file.write(strTime) 
                file.write(" :- ")
                file.write(note)
            
            else:
                speak("Okay sir, i have written the note without date and time") 
                file.write(note) 

        elif 'read note' in query or 'show note' in query:
            speak("Showing notes")
            file = open('data.txt', 'r')
            print(file.read())
            speak(file.read(6)) 




        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open snake game' in query:
            gamePath = "E:\\python\\pygame - snake game\\game.py"
            speak("Opening your snake game")
            os.startfile(gamePath) 

        # elif 'open camera' in query:
        #     cap = cv2.VideoCapture(0)
        #     while True:
        #         ret, img = cap.read()
        #         cv2.imshow('webcam', img) 
        #         k = cv2.waitKey(50)
        #         if k==27:
        #             break
        #         cap.release()
        #         cv2.destroyAllWindows()

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print(f"Your Ip address is: {ip}")
            speak(f"Sir, Your ip address is {ip}") 

        elif 'search something on google' in query:
            speak("What should i search on Google")
            cm = TakeCommand().lower()
            webbrowser.open(f"{cm}")

            speak(f"Searching for {cm} on google") 

        elif 'send message to me' in query:
            speak("What should i send to your number")
            whatMsg = TakeCommand().lower() 
            kit.sendwhatmsg("+918083175586", whatMsg,10,55 ) 

        elif 'who are you' in query:
            speak("Sir as i told, i am Jarvis, your assistant") 

        elif 'play a song on youtube'  in query: 
            speak("Sir which type of song sir")
            songType = TakeCommand().lower() 
            if 'romantic' in songType:
                Play_romantic_song() 
            elif 'dj' in songType:
                play_dj_song() 
            elif 'classic' in songType:
                play_classic_song()
            elif 'english' in songType:
                play_enlish_song()
            elif 'slow song' in songType:
                play_slow_song() 
            elif 'random' in songType:
                play_random_song() 
             

        elif 'doing great' in query or 'doing well' in query:
            doing_well_random = random.choice(doing_well) 
            print(doing_well_random) 
            speak(doing_well_random) 


        elif 'not good' in query or 'not well' in query or 'very bad' in query:
            unhappy_random = random.choice(unhappy)
            print(unhappy_random)
            speak(unhappy_random) 

        elif 'great' in query:
            great_random = random.choice(great)
            print(great_random)
            speak(great_random) 

        

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke(language="en")  
            speak(joke) 

        # my online classes

        elif 'set alarm' in query:
            speak("Sir, for which time you would like to set") 
            Alarm_time = (input("Enter the time for wwhich you want to set alarm: ")) 
            datef.alarm(Alarm_time) 
            speak(f"Sir, the alarm has been set for {hourA} : {minuteA}") 
            

        elif 'shutdown the system' in query:
            speak("Shutting off the system")
            os.system("shutdown /s /t 5") 
            
        elif 'restart the system' in query:
            speak("restarting off the system")
            os.system("shutdown /r /t 5")

        elif 'quit' in query or 'kuwait' in query: 
            print("Thanks for using me sir, have a good day")
            speak("Thanks for using me sir, have a good day") 
            sys.exit()

        elif 'where i am' in query or 'where we are' in query:
            speak("wait sir, let me check")
            try:
                url = 'https://get.geojs.io/v1/ip/geo/' + ip + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()

                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country'] 

                speak(f"sir i am not sure but i think we are in {city} city of {state}")
            
            except Exception as e:
                print(e) 
                print("Sorry sir i was not able to find our location due network issue") 
                speak("Sorry sir i was not able to find our location due network issue")

        # elif 'our location' in query:
        #     speak("wait sir let me check")

        #     send_url = 'http://freegeoip.net/json'
        #     r = requests.get(send_url)
        #     j = json.loads(r.text)
        #     lat = j['latitude']
        #     lon = j['longitude']

        #     speak(f"Sir your latitude is {lat}")
        #     speak(f"Sir your latitude is {lon}") 

        elif 'notification' in query:
            notification.notify(
                title = "Welcome to jarvis",
                message = "Sir, you have made me thank you, i am jarvis",
                app_icon = None,
                timeout = 10, 
            ) 
        
        elif 'take screenshot' in query or 'take a screenshot' in query:
            speak("Hold the screen for few seconds, i am taking screenshot")
            ScreenShot_name = TakeCommand().lower()
            # time.sleep(3)
            ScreenShot = pyautogui.screenshot()
            img.save(f"{ScreenShot_name}.png")
            speak("i am done sir, the image is saved in our main folder") 

        elif 'weather' in query:
            speak("Let me check sir") 
            try:
                res = app.query(query) 
                print(next(res.results).text) 
                speak(next(res.results).text) 
            
            except Exception as e:
                print(e) 

        elif 'read pdf' in query:
            pdf_reader()

        elif 'say that again please' in query:
            speak("i was not able to understand that") 

        elif 'battery status' in query or 'battery' in query: 
            cpu = str(psutil.cpu_percent()) 
            print(f"sir you have using {cpu} of your compuetr's cpu")
            speak(f"sir you have using {cpu} of your compuetr's cpu")  

            battery_left = psutil.sensors_battery().percent
            print(f"Sir your are left with {battery_left}")
            speak(f"Sir your are left with {battery_left}") 

        elif 'please' in query:
            speak("Sir tell me anything but don't tell please, i am your assistant") 

        elif 'jarvis give your introduction to my friends' in query or 'give your introduction' in query:
            speak(f"Hello, i am {Bot_name}, I am a genral porpuse bot made by Ashutosh, I am still In devlopment, i can do many things like sending messages on whatsapp, i search wikipedia,and do many more things like playing songs, checking social media messages setting alarm and timer,Telling the news, i can also feed you with the latest weather reports") 
             
            
              

        elif 'my location' in query or 'our location' in query:
            ch_number = phonenumbers.parse("+918083175586","CH")  
            geocoder.description_for_number(ch_number, "en-in") 

        elif 'timer' in query:
            speak("for how much seconds Sir")
            TimeToSet = int(input("For how much seconds Sir: ")) 
            for i in  range(TimeToSet):
                print(str(TimeToSet - 1) + " seconds remaining") 
                time.sleep(1) 

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt") 

        elif 'empty recycle bin' in query:
            speak("Are you sure sir you want to empty the recycle bin") 
            confirm = TakeCommand().lower() 
            if 'yes' in query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Recycled") 

            else:
                print("Okay sir")   
                speak("Okay sir")         

        elif 'scan qr code' in query:
            speak("opening camera sir!")  
            scan() 

        elif 'news' in query:
            speak("Sir wait for a while, i am feteching the latest news") 
            news() 

        elif 'weather' in query:
            CurrentWeather()   

        elif 'thank you jarvis' in query:
            print("It's my pleasure sir")
            speak("It's my pleasure sir") 

        
             


        elif 'doing well' in query:
            pass 
 

        # else:
        #     if '' in query:
        #         speak("Can you repeat it sir?")
        #         print("Can you repeat it sir?") 

        else:
            temp = query.replace(' ','+')  
            g_url = "https://www.google.com/search?q="
            res_g = "Sorry sir, i can't understant the query you have but let me search it on Google"
            print(res_g)
            speak(res_g)  
            webbrowser.open_new_tab(g_url+temp)  

        speak("Sir, do you have any other queries ?") 

        

        
            





        


    # speak("Sir, do you have any other work") 


        


        


        
        



