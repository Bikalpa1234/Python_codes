import cv2
import numpy as np
print('Package imported')

#import the image file
img = cv2.imread('C:\\Users\\DELL\\OneDrive\\Desktop\\Code\\me.png')
kernel=np.ones((5,5),np.uint8)
cv2.imshow("Output",img)
cv2.waitKey(0)

#First Thing To do after image is imported is to convert it to gray scale
imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray-Image",imgGray)
cv2.waitKey(0)

#Blurring Our Image
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Blur-Image",imgBlur)
cv2.waitKey(0)

#Edge Detector
imgCanny=cv2.Canny(img,100,100)  #threshold value determines the level of edge detection
cv2.imshow("Canny-Image",imgCanny)
cv2.waitKey(0)

#Increasing The thickness of the edge detection
imgDialation=cv2.dilate(imgCanny,kernel, iterations=1)
cv2.imshow("Dialated-Img",imgDialation)
cv2.waitKey(0)

#Opposite of dialation(make thinner)
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("Eroded image",imgEroded)
cv2.waitKey(0)

#Resize of the image
 #to find the size of image
print(img.shape)

imgResize=cv2.resize(img,(320,430))
cv2.imshow("Resized-Img",imgResize)
cv2.waitKey(0)

print(imgResize.shape)

#Cropping the image
imgCrop=img[0:200,200:500]
cv2.imshow("Cropped-Img",imgCrop)
cv2.waitKey(0)

#Drawing Shapes
draw=np.zeros((512,512,3),np.uint8)  #3 means allowing the color
print(draw.shape)
draw[:]=255,0,0 #drwa[:](means selecting the whole image)

#For Coloring the specific portion
draw[100:300,200:500]=0,255,0

#For Drwaing Line,rectangle,circle (similarly done!!)
cv2.line(draw,(0,0),(512,512),(0,0,255),3)
cv2.putText(draw,"Hello World!!",(250,250),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,50),5)


cv2.imshow("Drawing",draw)
cv2.waitKey(0)


cards= cv2.imread('C:\\Users\\DELL\\OneDrive\\Desktop\\Code\\cards.png')

width,height=250,250
pts1=np.float32([[106,49],[192,38],[126,179],[208,167]])    #https://www.mobilefish.com/services/record_mouse_coordinates/record_mouse_coordinates.php
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(cards,matrix,(width,height))


cv2.imshow("Cards",cards)
cv2.waitKey(0)
cv2.imshow("Img-Output",imgOutput)
cv2.waitKey(0)

#Joining the images together
hor=np.hstack((img,img))
ver=np.vstack((img,img))

cv2.imshow("Merged",hor)
cv2.imshow("Merged2",ver)
cv2.waitKey(0)

#Color Detection In Image
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
    imga= cv2.imread('C:\\Users\\DELL\\OneDrive\\Desktop\\Code\\me.png')
    imgHSV=cv2.cvtColor(imga,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue Min","Trackers")
    h_max=cv2.getTrackbarPos("Hue Max","Trackers")
    s_min=cv2.getTrackbarPos("Sat Min","Trackers")
    s_max=cv2.getTrackbarPos("Sat Max","Trackers")
    v_min=cv2.getTrackbarPos("Val Min","Trackers")
    v_max=cv2.getTrackbarPos("Val Max","Trackers")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max]) 
    mask=cv2.inRange(imgHSV,lower,upper)
    imgResult=cv2.bitwise_and(imga,imga,mask=mask)

    
    cv2.imshow("Original",imga)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Image-Result",imgResult)
    cv2.waitKey(1)






#import the video file
#cap=cv2.VideoCapture('video link goes here')

#while loop to go through each frame of the video
#while True:
    #success, img= cap.read()
    #cv2.imshow("Video",img)
    #if cv2.waitKey(1) & 0xFF ==ord('q'):
        #break

#to use the webcam

cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break






