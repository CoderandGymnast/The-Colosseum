from modules.countdown.const.HandCommands import HandCommands


class E_InputHand:
	def __init__(self) -> None:
		self._cmd=HandCommands.DEACTIVATE
		self._magnitude=0.0
  
	def getCMD(self):
		return self._cmd

	def setCMD(self,cmd):
		self._cmd=cmd
 
	def getMagnitude(self):
		return self._magnitude
 
	def setMagnitude(self,magnitude):
		self._magnitude=magnitude
