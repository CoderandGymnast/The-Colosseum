from modules.countdown.control.C_Control import C_Control
from os import umask
from tkinter import StringVar
from modules.countdown.entities.E_Watch import E_Watch
from ..control.C_Control import *

class E_CountdownWatch(E_Watch):
	def __init__(self, status):
		super().__init__(status)
		self.hours=StringVar()
		self.hours.set("00")
		self.mins=StringVar()
		self.mins.set("00")
		self.secs=StringVar()
		self.secs.set("05")
  
	def getTotalSecs(self):
		return int(self.hours.get())*3600 + int(self.mins.get())*60 + int(self.secs.get())

	def getHours(self):
		return self.hours

	def getMins(self):
		return self.mins

	def getSecs(self):
		return self.secs

	def setTime(self,hours,mins,secs):
		self.hours=hours
		self.mins=mins
		self.secs=secs
