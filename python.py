import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import serial




cap=cv2.VideoCapture(0)
detector=HandDetector(maxHands=1)
last_time = time.time()

while True:
    success,img=cap.read()
    hands,img=detector.findHands(img)
    if hands:
        hand=hands[0]
        fingers=detector.fingersUp(hand)
        current_time = time.time()
        if current_time - last_time >= 1:
            print(fingers)
            last_time = current_time
    cv2.imshow("HAND AND THEN FINGERS",img)
    if cv2.waitKey(1)==ord("A"):
        break