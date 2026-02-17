import speech_recognition as sr
from speech_recognition import Recognizer
recognizer = Recognizer()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio) # type: ignore
        return command
    except sr.UnknownValueError:
        return "Error: could not understand audio"
    except sr.RequestError:
        return "Error: could not request results"
print("please say something")
text = listen()
if text:
    print(f"You said: {text}")