import speech_recognition as sr
import os

def erkenne_sprache():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Bitte sprechen...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="de-DE")
        print(f"Erkannter Text: {text}")
    
        if "kartoffel" in text.lower() and "gulasch" in text.lower():
            print("Code is executing..")
            os.system("python control.py")
    
    except Exception:
        pass

if __name__ == "__main__":
    while True:
        erkenne_sprache()
