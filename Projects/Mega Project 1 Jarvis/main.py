import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.runAndWait()
    engine.say(text)
    

def processCommand(c):
    print(c)
    

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=4)
                word = recognizer.recognize_google(audio)
            if("jarvis" in word.lower):
                engine.s("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)
            
        except Exception as e:
            print("error; {0}".format(e))
