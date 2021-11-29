import pyttsx3    #text to speech 
import speech_recognition as sr    #speech recognizing
import datetime    #manipuates date and time
import wikipedia    #acess to data from wikipidea
import webbrowser    #webbrowser controller
import os    #interacts with operating system
import pyjokes    #jokes
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



def speak(audio):
    """This function will program AI to speak something"""
    
    engine.say(audio)
    engine.runAndWait()



def WishMe():
    """This function will program AI to wish user according to system line"""

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good afternoon") 
        print("Good afternoon") 
    else:
        speak("Good evening")
        print("Good evening")

    speak("This is your personal AI Morvi. Please tell me how can i help you ?") 
    print("This is your personal AI Morvi. Please tell me how can i help you ?") 



def takeCommand():
    """This function will program AI to take input from user and returns string output """


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:

        print("Sorry i couldn't understant. Say that again please..")
        return "None"      
    return query

    

def Task():

    speak("Hello, I am Morvi.")
    speak("How can I help you ?")

    if __name__ == "__main__":
        WishMe()

        while True:
            query = takeCommand().lower()

            #logic for executing task based on query
            
            if "wikipedia" in query:
                speak("searching wikipedia...")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("Accordind to wikipedia")
                print(results)
                speak(results)

            
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            
            elif 'open google' in query:
                webbrowser.open("google.com")

        
            #elif 'play music' in query:
                #music_dir = ""
                #songs=os.listdir(music_dir)
                #print(songs)
                #os.startfile(os.path.join(music_dir,songs[0]))

            
            elif 'the time' in query :
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                speak(f"The time is {strTime}")
                print(strTime)

            
            elif 'open note' in query:
                notepad = "%windir%\\system32\\notepad.exe"
                os.startfile(notepad)
            
            elif 'open word' in query:
                wordpad = "C:\\Program Files\\Windows NT\\Accessories\\wordpad.exe"
                os.startfile(wordpad)    
            

            elif 'open paint' in query:
                paint = "C:\\Program Files\\Windows NT\\Accessories\\Paint.exe"
                os.startfile(paint)   
        

            elif 'open code' in query:
                codePath = "C:\\Users\\Aditnotech\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)


            elif 'linkedin' in query:
                webbrowser.open("https://www.linkedin.com")


            elif 'facebook' in query:
                webbrowser.open("https://www.facebook.com")

            
            #elif 'open email' in  query:


            elif 'joke' in query:
                jokes1 = pyjokes.get_joke()
                print(jokes1)
                speak(jokes1)

            elif 'alarm' in query:
                    speak("Enter The Time !")
                    time = input(": Enter The Time :")

                    while True:
                        Time_Ac = datetime.datetime.now()
                        now = Time_Ac.strftime("%H:%M:%S")

                        if now == time:
                            speak("Time To Wake Up Sir!")
                            playsound('ringtone.mp3')
                            print('playing sound using  playsound')
                            speak("Alarm Closed!")
                            print("Alarm Closed!")

                        elif now>time:
                            break  

            elif 'you need a break' in query:
                speak("Ok Sir, You can call me anytime !")
                speak("Just say Wake Up Morvi !")
                break
            
            
Task()



        
         
            


                

        
