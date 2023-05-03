import cv2
import numpy as np
clr = input("Enter the colour to be isolated out of: blue, ")
cap= cv2.VideoCapture(0)
while 1:
    ret, frame= cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    L_limit=np.array([98,50,50])
    U_limit=np.array([139,255,255])
    b_mask=cv2.inRange(hsv,L_limit,U_limit)
    blue =cv2.bitwise_and(frame,frame,mask=b_mask)
    cv2.imshow("original", frame)
    cv2.imshow('blue', blue)
    key = cv2.waitKey(1)
    if key==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()