import cv2
import sys, time, os

from time import sleep

#creacion de objetos
video_capture = cv2.VideoCapture(0)
video_capture.set(3,420)
video_capture.set(4,280)

cap = cv2.VideoCapture(1)
cap.set(3,320)
cap.set(4,180)

#cap2 = cv2.VideoCapture(2)
#cap2.set(3,320)
#cap2.set(4,180)

i=0
dirname= 'camera'
os.chdir(dirname)
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow('frame', gray)
localtime = time.asctime( time.localtime(time.time()))
cv2.imwrite('cam1-'+str(i) + localtime + '.jpg', frame)
i += 1
cap.release()
cv2.destroyWindow("frame")
