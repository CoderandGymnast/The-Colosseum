import cv2
import numpy as np
import S_HandTracker as sht
import time
import autopy
from numpy import linalg as la

##########################
wCam, hCam = 640, 480
frameR = 100 # Frame Reduction
smoothening = 7
#########################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, wCam)
cap.set(4, hCam)
tracker = sht.S_HandTracker(maxHands=1)
wScr, hScr = autopy.screen.size()
# print(wScr, hScr)

count=0
# dis8To17s=np.empty(0)
while True:
    
	# if count==1000:
	# 	print(np.std(dis8To17s))
	# 	break
    
	count+=1
	# 1. Find hand Landmarks
	success, img = cap.read()
	img = tracker.findHands(img)
	lmList, bbox = tracker.findPosition(img)
	# print(len(lmList)) # 21.
	# 2. Get the tip of the index and middle fingers
	if len(lmList) != 0:
		x8, y8 = lmList[8][1:]
		x12, y12 = lmList[12][1:]
		x17, y17=lmList[17][1:]
		# dis8To17=la.norm(np.subtract([x8,y8],[x17,y17]))
		# dis8To17s=np.append(dis8To17s,dis8To17)
		# print(x1, y1, x2, y2)
	
	# 3. Check which fingers are up
	fingers = tracker.fingersUp()
	# print(fingers)
	cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
	(255, 0, 255), 2)
	
	if fingers:
		# 4. Only Index Finger : Moving Mode
		if fingers[1] == 1 and fingers[2] == 0:
			# 5. Convert Coordinates
			x3 = np.interp(x8, (frameR, wCam - frameR), (0, wScr))
			y3 = np.interp(y8, (frameR, hCam - frameR), (0, hScr))
			# 6. Smoothen Values
			clocX = plocX + (x3 - plocX) / smoothening
			clocY = plocY + (y3 - plocY) / smoothening
		
			# 7. Move Mouse
			autopy.mouse.move(wScr - clocX, clocY)
			cv2.circle(img, (x8, y8), 15, (255, 0, 255), cv2.FILLED)
			plocX, plocY = clocX, clocY
			
		# 8. Both Index and middle fingers are up : Clicking Mode
		if fingers[1] == 1 and fingers[2] == 1:
			# 9. Find distance between fingers
			length, img, lineInfo = tracker.findDistance(8, 12, img)
			# print(length)
			# 10. Click mouse if distance short
			if length < 40:
				cv2.circle(img, (lineInfo[4], lineInfo[5]),
				15, (0, 255, 0), cv2.FILLED)
				autopy.mouse.click()
	
	# 11. Frame Rate
	cTime = time.time()
	fps = 1 / (cTime - pTime)
	pTime = cTime
	cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
	(255, 0, 0), 3)
	# 12. Display
	cv2.imshow("Image", img)
	cv2.waitKey(1)
