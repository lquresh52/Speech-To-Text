import speech_recognition as sr  
import pyaudio
r= sr.Recognizer()
with sr.Microphone() as source:
    print ("Speek anything")
    audio=r.listen(source)
    try:
        text= r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize")
