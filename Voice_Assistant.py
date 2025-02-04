import pyttsx3
import pywhatkit 
import pyautogui
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

while True:
    query = input("Me :-")
    if "your name" in query:
        speak("My name is Bawa Ji")
        print("My name is Bawa Ji")
        speak("What is your good name :")
        q = input("What is your good name :")
        print(f"{q} nice name")
        speak(f"{q} nice name")
        
    elif "open google" in query:
        speak("Opening Google")
        print("Opening Google")
        speak("What should i search for you :")
        print("What should i search for you :")
        q = input("What should i search for you :")
        pywhatkit.search(q)
        webbrowser.open("httpL://www.google.com")
        
    elif "open youtube" in query:
        speak("Opening YouTube")
        print("Opening YouTube")
        speak("What should i search for you :")
        print("What should i search for you :")
        q = input("What should i search for you :")
        pywhatkit.search(q)
        webbrowser.open("httpL://www.youtube.com")
        
    elif "volume down" in query:
        speak("Volume decreased")
        print("Volume decreased")
        pyautogui.press('volumedown')

        
    elif "exit" in query:
        speak("Good Bye")
        print("Good Bye")
        exit()