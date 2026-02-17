import pyttsx3

def get_english_voice(engine):
    Voices = engine.getProperty('voices')
    for voice in Voices:
        if 'English' in voice.id or (voice.languages and "en" in voice.launguages[0]):
            return voice.id


def to_voice(text):
    engine = pyttsx3.init()


    engine.setProperty('rate', 175)  # Speed percent (can go over 100)
    engine.setProperty('volume', 1)  # Volume 0-1

    voices = engine.getProperty('voices')

    

    if isinstance(voices, (list, tuple)) and voices:
        engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()
    engine.stop()


def main():
    text = input("Enter the text you want to convert to voice: ")
    to_voice(text)  

if __name__ == "__main__":
    main()