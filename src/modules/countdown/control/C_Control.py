import _thread

from cv2 import magnitude
from modules.countdown.const.HandCommands import HandCommands
from modules.countdown.const.Values import Commands, responses,Responses, commands
from modules.countdown.entities.E_InputVoice import AMBIENT_NOISE
import time

class C_Control:
	def __init__(self,mainGUI,sListener,sSpeaker,sWatcher,eInputVoice,eInputHand,eWatch):
		self.mainGUI=mainGUI
		self.sListener=sListener
		self.sSpeaker=sSpeaker
		self.sWatcher=sWatcher
		self.eInputVoice=eInputVoice
		self.eInputHand=eInputHand
		self.eWatch=eWatch
	
	def process(self):
		workers=[self.listenningWorker,self.handlingWorker,self.greetingWorker,self.watchingWorker]
		try:
			for worker in workers:
				self.startWorker(worker)
			self.mainGUI.process()
		except Exception as e:
			''''''

	def startWorker(self,job):
		_thread.start_new_thread(job,("",))

	def greetingWorker(self,name):
		self.sSpeaker.say(responses[Responses.GREETING])
		self.sSpeaker.say(responses[Responses.SELECT_TIME])

	def countDownGUIWorker(self,name):
		self.mainGUI.countdownGUI.countDown()
  
	def listenningWorker(self,name):
		self.sListener.process()
  
	def handlingWorker(self,name):
     
		# [NOTE]: Hand Gesture.
		tab=0.0
		#---
     
		while 1:
			print(self.eInputHand.getMagnitude())
			time.sleep(0.001)
			
   			# [NOTE]: Hand Gesture.
			handCMD=self.eInputHand.getCMD()
			magnitude=self.eInputHand.getMagnitude()
			if handCMD == HandCommands.VOLUME:
				if 2.0 < tab: # [NOTE]: Set hours.
					if 0 <= magnitude and magnitude <= 24:
						self.mainGUI.countdownGUI.setHours(magnitude)
      
				if 1.0 < tab and tab <= 2.0: # [NOTE]: Set mins.
					if 0 <= magnitude and magnitude <= 60:
						self.mainGUI.countdownGUI.setMins(magnitude)
      
				if tab<=1.0: # [NOTE]: Set mins.
					if 0 <= magnitude and magnitude <= 60:
						self.mainGUI.countdownGUI.setSecs(magnitude)
      
			if handCMD == HandCommands.TAB: # [NOTE]: Change tabs.
				tab=magnitude
				if 2.0 < tab:
					self.mainGUI.countdownGUI.focusHours()
				if 1.0 < tab and tab <= 2.0:
					self.mainGUI.countdownGUI.focusMins()
				if tab<=1.0:
					self.mainGUI.countdownGUI.focusSecs()

					

			#---
      
			inputValue=self.eInputVoice.getValue()
			if not inputValue:
				continue
			if inputValue.find(commands[Commands.GO]) != -1:
    
				self.sSpeaker.say(responses[Responses.WAIT_COUNTING])
				count=3
				while count:
					self.sSpeaker.say(count)
					count=count-1
				
				self.sSpeaker.say(responses[Responses.START_COUNTING])
				count=self.eWatch.getTotalSecs()
				self.startWorker(self.countDownGUIWorker)
				while count:
					time.sleep(1)
					count=count-1
				self.sSpeaker.say(responses[Responses.TIME_UP])			
   
				self.eInputVoice.resetValue()
				continue
			if inputValue.find(AMBIENT_NOISE) != 0:
				''''''
	def watchingWorker(self,name):
		self.sWatcher.process()
