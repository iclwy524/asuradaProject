#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()

class ear:
    def __init__(self,recogSource):
        self.recogSource=recogSource;


    def listening(self):
        with sr.Microphone() as source:
            print("Say something! Analysis by "+self.recogSource)
            audio = r.listen(source)

        try:
            processedMsg=r.recognize_sphinx(audio)
            print(processedMsg)
            return(processedMsg)

        except sr.UnknownValueError:
            print("Can't understand what you said")
        except sr.RequestError as e:
            print ("Sphinx error; {0}".format(e))


if __name__=="__main__":
    earMsg=ear("phinx")
    earMsg.listening()
