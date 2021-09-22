from tkinter import READABLE
from modules.countdown.const.Values import Responses,responses
import pyttsx3 as tts
import time
import random

class S_Speaker:
    def __init__(self):
        engine=tts.init()
        voices=engine.getProperty("voices")
        engine.setProperty("voice",voices[1].id)
        self.engine=engine
        
    def say(self,text):
        self.engine.say(text)
        self.engine.runAndWait()
        
    def countDown(self, totalTime):
        
        self.say(responses[Responses.WAIT_COUNTING])
        count=3
        while count:
            # time.sleep(0.5)
            self.say(count)
            count=count-1
        i = random.randint(0, len(responses[Responses.START_COUNTING]))
        self.say(responses[Responses.START_COUNTING][i])
        
        count=totalTime
        while count:
            time.sleep(1)
            # self.say(count)
            count=count-1
            if count<=5: self.say(count)
        
        i = random.randint(0, len(responses[Responses.TIME_UP]))
        self.say(responses[Responses.TIME_UP][i])
