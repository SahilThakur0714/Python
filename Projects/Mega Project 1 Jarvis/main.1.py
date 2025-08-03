import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
# newsapi = ""

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(f"Processing: {c}")
    # Add command handling logic here
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c:
        # r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles
            articles = data. get('articles', [])
            print(f"Articles received: {len(articles)}")

            # Print the headlines
            for article in articles:
                print(f"Saying: {article['title']}") 
                engine.say(article['title'])
                engine.runAndWait()
    else:
        # let openAI handle the request
        pass


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word ('Jarvis')...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)

                print(f"Heard: {word}")

                if "jarvis" in word.lower():
                    engine.say("Yes")
                    
                    with sr.Microphone() as source:
                        print("Listening for your command...")
                        recognizer.adjust_for_ambient_noise(source, duration=1)
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
                        command = recognizer.recognize_google(audio)

                        processCommand(command)
                else:
                    print("Wake word not detected.")

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Request error from Google API: {e}")
        except Exception as e:
            print(f"Other error: {e}")
