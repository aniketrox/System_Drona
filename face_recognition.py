import cv2
import os
from PIL import Image,ImageTk
import numpy as np
#import System_Drona.views

#id= System_Drona.views.id

ide ={1:"Rohit",2:"Aniket",3:"Disha",4:"Risav"}






def face_recog():
    temp = 1
    def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
        gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
        coord = []
        
        for (x,y,w,h) in features:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
            id,predict=clf.predict(gray_image[y:y+h,x:x+w])
            confidence = int((100*(1-predict/300)))
            
            if confidence>77:
                cv2.putText(img,f"NAME:{ide[id]}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                temp = 0
            else:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                cv2.putText(img,"unknown face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
            
            coord = [x,y,w,y]
        
        return coord
    
    def recognize(img,clf,faceCascade):
        coord = draw_boundary(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
        return img
    
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")
    
    video_cap = cv2.VideoCapture(0)
    
    while True:
        ret,img = video_cap.read()
        img = recognize(img, clf, faceCascade)
        cv2.imshow("Welcome to Face Recognition",img)
        
        if cv2.waitKey(1)==13:
            break
    
    video_cap.release()
    cv2.destroyAllWindows()
    
            
            

face_recog()  
    
#generate_dataset()