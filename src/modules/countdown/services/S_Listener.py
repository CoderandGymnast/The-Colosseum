from modules.countdown.entities.E_Input import E_Input
from speech_recognition import UnknownValueError, RequestError
import speech_recognition as sr

class S_Listener:
    def __init__(self,eInput):
	    self.eInput=eInput

    def process(self):
        
        m = sr.Microphone()    

        try:
            while True:
                r = sr. Recognizer()
                with m as source: r.adjust_for_ambient_noise(source)     
                print(f"Based on the environment, automatically set minimum energy threshold (volume) to {r.energy_threshold}")
                print("Listening...")
                with m as source: audio = r.listen(source)
                print("Processing..")
                try:
                    value = r.recognize_google(audio)
                    print((f"Command: '{value.capitalize()}'"))
                    self.eInput.setValue(value)
                except UnknownValueError:
                    self.eInput.toAmbientNoise()
                    print("[WARNING]: Ambient noise")
                except RequestError as e:
                    print("[WARNING]: Google Speech Recognition service: '{0}'".format(e))
        except KeyboardInterrupt:
            pass
     
