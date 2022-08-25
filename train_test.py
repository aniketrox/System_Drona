import cv2
import os
from PIL import Image,ImageTk
import numpy as np
#import System_Drona.views

#id= System_Drona.views.id

ide ={1:"Rohit",2:"Aniket",3:"Disha",4:"Risav"}



def train_classifier():
    data_dir=("data")
    path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
    
    faces = []
    ids = []
    
    for image in path:
        img = Image.open(image).convert('L')
        imageNp = np.array(img,'uint8')
        id = int(os.path.split(image)[1].split('.')[1])
        
        faces.append(imageNp)
        ids.append(id)
        cv2.imshow("Training",imageNp)
        cv2.waitKey(1)==13
    
    ids=np.array(ids)
    
    # training the classifier and save
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces,ids)
    clf.write("classifier.xml")
    cv2.destroyAllWindows()
    print("Training dataset completed")
    
    
    
def generate_dataset():
    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
    
    id = list(ide.keys())[0]
    def face_cropped(img):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray,1.3,5)
        
        for (x,y,w,h) in faces:
            face_cropped=img[y:y+h,x:x+w]
            return face_cropped
        
    cap = cv2.VideoCapture(0)
    org = (50,50)
    img_id = 0
    while True:
        ret, my_frame=cap.read()
        if face_cropped(my_frame) is not None:
            img_id+=1
            face = cv2.resize(face_cropped(my_frame),(450,450))
            face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
            file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
            cv2.imwrite(file_name_path, face)
            cv2.putText(face,str(img_id),org,cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
            cv2.imshow("cropped face",face)
        
        if cv2.waitKey(1)==13 or int(img_id)==200:
            break
    cap.release()
    cv2.destroyAllWindows()
    print("Generating dataset completed.")
    train_classifier()
            
    


    
generate_dataset()