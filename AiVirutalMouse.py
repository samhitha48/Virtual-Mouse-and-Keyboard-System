import cv2
import autopy
import time
import numpy as np
import HandTrackingModule as htm

############################
wCam, hCam = 640, 480
frameR = 100 # Frame Reduction
smoothening = 7
############################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()


mouse_position = (0, 0)
mouse_down = False
mouse_button = None 
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if len(lmList)!=0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        

        
        fingers = detector.fingersUp()
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                      (255, 0, 255), 2)
        # 4. Only index Finger :Moving Mode
        if fingers[1] == 1 and fingers[2] == 0:
            # 5. convert coordinates

            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))
            # 6. Smoothen Values
            clocX = plocX +(x3 -plocX) /smoothening
            clocY = plocY + (y3 - plocY) / smoothening
            #7. Mouse Move 
            autopy.mouse.move(wScr-clocX, clocY)
            cv.2circle(img (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY
            
        # 8. Both Index and Middle Finger are up : Clicking Mode
        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            print(length)
            if length < 39:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                           15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()
        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            print(length)
            if (length> 39):
                pyautogui.click(button='right')
        if fingers[3]==1  
        pyautogui.scroll(-2)
        if fingers[2]==1  
        pyautogui.scroll(2)

    cv2.imshow("Virtual Mouse", img)
    cv2.waitKey(100)
