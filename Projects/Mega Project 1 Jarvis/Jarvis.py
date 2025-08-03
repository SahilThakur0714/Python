import speech_recognition as sr
import webbrowser
import pyttsx3
import time

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Configure TTS engine for better speech
def configure_tts():
    """Configure the text-to-speech engine"""
    voices = engine.getProperty('voices')
    if voices:
        # Try to set a male voice (usually index 0)
        engine.setProperty('voice', voices[0].id)
    
    # Set speech rate (words per minute)
    engine.setProperty('rate', 180)  # Default is usually 200
    
    # Set volume (0.0 to 1.0)
    engine.setProperty('volume', 0.9)

configure_tts()

def speak(text):
    """Convert text to speech"""
    print(f"Jarvis: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
        print("Speech completed")  # Debug message
    except Exception as e:
        print(f"TTS Error: {e}")
        # Fallback - try reinitializing the engine
        try:
            global engine
            engine.stop()
            engine = pyttsx3.init()
            configure_tts()
            engine.say(text)
            engine.runAndWait()
        except:
            print("TTS completely failed - check audio drivers")

def processCommand(command):
    """Process the voice command"""
    print(f"Command received: {command}")
    
    # Add some basic commands
    command = command.lower()
    
    if "open google" in command:
        speak("Opening Google sir!")
        webbrowser.open("https://google.com")
    elif "open youtube" in command:
        speak("Opening YouTube sir!")
        webbrowser.open("https://youtube.com")
    elif "hello" in command:
        speak("Hello sir! How can I help you?")
    elif "time" in command:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time} sir")
    elif "stop" in command or "exit" in command:
        speak("Goodbye sir!")
        return False
    else:
        speak("I didn't understand that command sir")
    
    return True

def listen_for_wake_word():
    """Listen for the wake word 'Jarvis'"""
    try:
        with sr.Microphone() as source:
            print("Listening for wake word...")
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            # Listen with shorter timeout to avoid hanging
            audio = recognizer.listen(source, timeout=1, phrase_time_limit=3)
            word = recognizer.recognize_google(audio, language='en-US')
            print(f"Heard: {word}")
            
            if "jarvis" in word.lower():
                return True
    except sr.WaitTimeoutError:
        # This is normal - just means no speech was detected
        pass
    except sr.UnknownValueError:
        # Speech was unintelligible
        pass
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"Error in wake word detection: {e}")
    
    return False

def listen_for_command():
    """Listen for a command after wake word is detected"""
    try:
        with sr.Microphone() as source:
            print("Jarvis Active... Listening for command...")
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            # Listen for command
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio, language='en-US')
            return command
    except sr.WaitTimeoutError:
        speak("I didn't hear anything")
        return None
    except sr.UnknownValueError:
        speak("I couldn't understand what you said")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    except Exception as e:
        print(f"Error in command recognition: {e}")
        return None

if __name__ == "__main__":
    # Test TTS first
    print("Testing text-to-speech...")
    speak("Text to speech is working sir!")
    
    speak("Initializing Jarvis sir...")
    print("Jarvis is ready! Say 'Jarvis' to wake me up.")
    
    try:
        while True:
            # Listen for wake word
            if listen_for_wake_word():
                speak("Yes, how can I help you?")
                
                # Listen for command
                command = listen_for_command()
                if command:
                    # Process the command
                    continue_running = processCommand(command)
                    if not continue_running:
                        break
                
                # Small delay before listening for wake word again
                time.sleep(0.5)
            
            # Small delay to prevent excessive CPU usage
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nShutting down Jarvis...")
        speak("Goodbye!")
    except Exception as e:
        print(f"Fatal error: {e}")
        speak("Sorry, I encountered an error and need to shut down")