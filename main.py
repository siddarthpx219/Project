import speech_recognition 
import pyttsx3
import wikipedia 
import webbrowser

recognizer = speech_recognition.Recognizer()
engine = pyttsx3.init()

def speak (text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = 
        webbrowser.open(link)

def query_resolution(query):
    try:
        summary = wikipedia.summary(query, sentences=2) 
        speak(summary)
        return True
    except wikipedia.PageError:
        speak("Sorry, I couldn't find anything related to " + query + " on Wikipedia.")
        return False        


if __name__ == "__main__":
    speak("Initializing Lisa")
    while True:
        r = speech_recognition.Recognizer()
         
        print("recognizing")
        try:
            with speech_recognition.Microphone() as source:
                print("Listening")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "Lisa"):
                speak("Yes")
                # Listen for command
                with speech_recognition.Microphone() as source:
                    print("Lisa Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    query = r.recognize_google(audio)

         if(query.lower().startswith("who")):
            query_resolution(query)
         elif(query.lower().startswith("who")):
            query_resolution(query)
         elif(command.lower().startswith("open") or command.lower().startswith("play")):
            processCommand(command)

                    
            except Exception as e:
            print("Error; {0}".format(e))

