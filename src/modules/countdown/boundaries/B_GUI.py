import time
from tkinter import *
import tkinter.font as font

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

	def setHours(self,value):
		self.hours.set(value)
		self.eHours.focus()
		self.root.update()
 
	def setMins(self,value):
		self.mins.set(value)
		self.eMins.focus()
		self.root.update()
  
	def setSecs(self,value):
		self.secs.set(value)
		self.eSecs.focus()
		self.root.update()
  
	def focusHours(self):
		self.eHours.focus()
		self.root.update()
  
	def focusMins(self):
		self.eMins.focus()
		self.root.update()
  
	def focusSecs(self):
		self.eSecs.focus()
		self.root.update()
  
	def init(self):
		self.initUIWidgets()
  
	def setTime(self,hours,mins,secs):
			self.hours.set("00" if not hours else hours)
			self.mins.set("00" if not mins else mins)
			self.secs.set(secs)
  
	def initUIWidgets(self):
		self.eHours=Entry(self.frame, font=self.eFont,bg=self.background,fg=self.textColor,bd=0,width=2,textvariable=self.hours,insertbackground="red")
		self.eHours.place(x=30 ,y=35)

		lColon=Label(self.frame, font=self.eFont,bg=self.background,fg=self.textColor,text=":")
		lColon.place(x=100 ,y=35)

		self.eMins=Entry(self.frame, font=self.eFont,bg=self.background,fg=self.textColor,bd=0,width=2,textvariable=self.mins,insertbackground="red")
		self.eMins.place(x=130 ,y=35)

		lColon=Label(self.frame, font=self.eFont,bg=self.background,fg=self.textColor,text=":")
		lColon.place(x=200 ,y=35)

		self.eSecs=Entry(self.frame, font=self.eFont,bg=self.background,fg=self.textColor,bd=0,width=2,textvariable=self.secs,insertbackground="red")
		self.eSecs.place(x=230,y=35)
		
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

			hours=self.add0(hours) if hours < 10 else hours
			mins=self.add0(mins) if mins < 10 else mins
			secs = self.add0(secs) if secs < 10 else secs
			self.setTime(hours,mins,secs)
		
			self.root.update()
			time.sleep(1)
			totalSecs -= 1
   
	def add0(self,v):
		return f"0{v}"
        
   
	

