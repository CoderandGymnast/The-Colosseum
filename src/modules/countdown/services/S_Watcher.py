from tkinter.constants import S
import cv2
import numpy as np
import time
from modules.countdown.const.HandCommands import HandCommands
import math

class S_Watcher:
	def __init__(self,eInputHand,sHandTracker) -> None:
		self.eInputHand=eInputHand
		self.wCam, self.hCam = 640, 480
		self.frameR = 50
		self.smoothening = 7
		self.pTime = 0
		self.plocX, self.plocY = 0, 0
		self.clocX, self.clocY = 0, 0
  
		cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
		cap.set(3, self.wCam)
		cap.set(4, self.hCam)
		self.cap=cap
		self.sHandTracker = sHandTracker 
  
	def process(self):
		while True:
			success, img = self.cap.read()
			img = self.sHandTracker.findHands(img)
			lmList, bbox = self.sHandTracker.findPosition(img)
			if len(lmList) != 0:
				x8, y8 = lmList[8][1:]
				x12, y12 = lmList[12][1:]
				x17, y17=lmList[17][1:]
			fingers = self.sHandTracker.fingersUp()
			cv2.rectangle(img, (self.frameR, self.frameR), (self.wCam - self.frameR, self.hCam - self.frameR),
			(255, 0, 255), 2)
			
			if fingers:
				if fingers[1] == 1 and fingers[2] == 0:
					self.eInputHand.setCMD(HandCommands.VOLUME)
					self.eInputHand.setMagnitude(math.floor((y8-100)/4))

					
				if fingers[1] == 1 and fingers[2] == 1:
					self.eInputHand.setCMD(HandCommands.TAB)
					self.eInputHand.setMagnitude((x8-50)/160)
      
				if fingers[1] and fingers[2] and fingers[3]:
					self.eInputHand.setCMD(HandCommands.DEACTIVATE)
			else:
				self.eInputHand.setCMD(HandCommands.DEACTIVATE)
     
      
			# cTime = time.time()
			# fps = 1 / (cTime - self.pTime)
			# self.pTime = cTime
			# cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
			# (255, 0, 0), 3)
			# cv2.imshow("Image", img)
			# cv2.waitKey(1)

