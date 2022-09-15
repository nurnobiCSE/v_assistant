import speech_recognition as sr
import wikipedia
import pywhatkit
import pyttsx3

listner = sr.Recognizer()
engine = pyttsx3.init()

def runAssist():
    engine.say("this is assist")
    engine.say("how can i help you ?")
    engine.runAndWait()
    listen()

def listen():
    try:
        while(True):
            engine.runAndWait()
            with sr.Microphone() as src:
                print("listening....")
                voice = listner.listen(src)
                cmd = listner.recognize_google(voice)
                cmd = cmd.lower()

                if 'jony' in cmd:
                    cmd = cmd.replace('jony', '')
                    process(cmd)
                elif 'stop' in cmd:
                    stop()

    except:
        pass
def process(cmd):
    if 'play' in cmd:
        playvideo(cmd)
    elif 'tell me about' in cmd:
        searchinfo(cmd)

def playvideo(cmd):
    cmd = cmd.replace('play','')
    engine.say("just give me a second! \n playing your song..." + cmd)
    engine.runAndWait()
    pywhatkit.playonyt(cmd)

def searchinfo(cmd):
    cmd = cmd.replace('tell me about','')
    engine.say(wikipedia.summary(cmd,sentances=3).replace('listen',''))
    engine.runAndWait()

def stop():
    engine.say("good by boss !")
    engine.runAndWait()
    exit()

runAssist()
