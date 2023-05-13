import cv2

#adding the face cascade
faceCascade= cv2.CascadeClassifier('C:\\Users\\DELL\\OneDrive\\Desktop\\Code\\face.xml')
img= cv2.imread('C:\\Users\\DELL\\OneDrive\\Desktop\\Code\\me.png')

#converting image to greyscale
imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    

cv2.imshow("Result",img)
cv2.waitKey(0)
