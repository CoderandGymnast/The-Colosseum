from typing import List
from speech_recognition import UnknownValueError, RequestError
import speech_recognition as sr

class Listener():
    
    def log(self, mess):
        print(mess)

    def process(self):
        
        m = sr.Microphone()    

        try:
            while True:
                r = sr. Recognizer()
                with m as source: r.adjust_for_ambient_noise(source)     
                self.log(f"Based on the environment, automatically set minimum energy threshold (volume) to {r.energy_threshold}")
                self.log("Listening...")
                with m as source: audio = r.listen(source)
                self.log("Processing..")
                try:
                    value = r.recognize_google(audio)
                    self.log((f"Command: '{value.capitalize()}'"))
                except UnknownValueError:
                    self.log("[WARNING]: Ambient noise")
                except RequestError as e:
                    self.log("[WARNING]: Google Speech Recognition service: '{0}'".format(e))
        except KeyboardInterrupt:
            pass
        
        
listener=Listener()
listener.process()

