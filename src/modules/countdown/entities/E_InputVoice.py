AMBIENT_NOISE="0"

class E_InputVoice:
    def __init__(self):
        self._value=None
        
    def setValue(self,value):
        self._value=value.upper()
    
    def getValue(self):
        return self._value
    
    def resetValue(self):
        self._value=None
        
    def toAmbientNoise(self):
        self._value=AMBIENT_NOISE
