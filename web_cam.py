import cv2
import numpy as np

cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

def empty(a):
    pass

cv2.namedWindow("Trackers")
cv2.resizeWindow("Trackers",640,240)
cv2.createTrackbar("Hue Min","Trackers",39,179,empty)
cv2.createTrackbar("Hue Max","Trackers",103,179,empty)
cv2.createTrackbar("Sat Min","Trackers",126,255,empty)
cv2.createTrackbar("Sat Max","Trackers",255,255,empty)
cv2.createTrackbar("Val Min","Trackers",27,255,empty)
cv2.createTrackbar("Val Max","Trackers",255,255,empty)


while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue Min","Trackers")
    h_max=cv2.getTrackbarPos("Hue Max","Trackers")
    s_min=cv2.getTrackbarPos("Sat Min","Trackers")
    s_max=cv2.getTrackbarPos("Sat Max","Trackers")
    v_min=cv2.getTrackbarPos("Val Min","Trackers")
    v_max=cv2.getTrackbarPos("Val Max","Trackers")
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max]) 
    mask=cv2.inRange(imgHSV,lower,upper)
    #imgResult=cv2.bitwise_and(img,img,mask=mask)


    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    #cv2.imshow("Image-Result",imgResult)
    cv2.waitKey(1)


    if cv2.waitKey(1) & 0xff ==ord('q'):
        break