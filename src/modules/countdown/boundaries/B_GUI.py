import time
from tkinter import *
import tkinter.font as font

from modules.countdown.entities.E_Watch import E_Watch

class B_GUI:
	def __init__(self, root,frame,eWatch):
		self.eWatch=eWatch
		self.root=root
		self.frame=frame
		self.eFont= font.Font(root,family="Arial", size=40)
		self.lFont= font.Font(root,family="Arial", size=10)
		self.background="#0e1013"
		self.textColor="#7f7f7f"
		self.hours=self.eWatch.getHours()
		self.mins=self.eWatch.getMins()
		self.secs=self.eWatch.getSecs()

		self.init()	
 
	def init(self):
		self.initUIWidgets()
  
	def setTime(self,hours,mins,secs):
			self.hours.set("00" if not hours else hours)
			self.mins.set("00" if not mins else mins)
			self.secs.set(secs)
  
	def initUIWidgets(self):
		ehours=Entry(self.frame, font=self.eFont,bg=self.background,fg=self.textColor,bd=0,width=2,textvariable=self.hours)
		ehours.place(x=30 ,y=35)

		lColon=Label(self.frame, font=self.eFont,bg=self.background,fg=self.textColor,text=":")
		lColon.place(x=100 ,y=35)

		eMins=Entry(self.frame, font=self.eFont,bg=self.background,fg=self.textColor,bd=0,width=2,textvariable=self.mins)
		eMins.place(x=130 ,y=35)

		lColon=Label(self.frame, font=self.eFont,bg=self.background,fg=self.textColor,text=":")
		lColon.place(x=200 ,y=35)

		eSecs=Entry(self.frame, font=self.eFont,bg=self.background,fg=self.textColor,bd=0,width=2,textvariable=self.secs)
		eSecs.place(x=230,y=35)
		
		lHours=Label(self.frame, font=self.lFont,bg=self.background,fg=self.textColor,text="HOURS")
		lHours.place(x=(320-260)/2 + 5 ,y=110)

		lMins=Label(self.frame, font=self.lFont,bg=self.background,fg=self.textColor,text="MINUTES")
		lMins.place(x=(320-260)/2 + 100,y=110)

		lSecs=Label(self.frame, font=self.lFont,bg=self.background,fg=self.textColor,text="SECONDS")
		lSecs.place(x=(320-260)/2 + 200 - 5,y=110)


	def countDown(self):
		totalSecs=self.eWatch.getTotalSecs()
		while totalSecs >-1:
			
			mins,secs = divmod(totalSecs,60)
			hours=0
			if mins >60:
				hours, mins = divmod(mins, 60)
   
			self.setTime(hours,mins,secs)
		
			self.root.update()
			time.sleep(1)
			totalSecs -= 1
   
	

