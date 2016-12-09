#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import pyttsx
import os

class mouth:
    def __init__(self):
        self.speech_engine=pyttsx.init('nsss')
        self.speech_engine.setProperty('rate',150)


    def speaking(self,msgToSpeak):
        try:
            print (msgToSpeak)
            ##self.speech_engine.say("i guess you've said "+msgToSpeak)
            #self.speech_engine.runAndWait()
            os.system("say "+msgToSpeak)
            exit()
        except:
            print("cannot speak")
if __name__ == "__main__":
    speak=mouth()
    speak.speaking("how are you")
