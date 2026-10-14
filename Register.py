import tkinter as tk
import tkinter.font as font
import tkinter.ttk as ttk
from tkinter import *
import os
import sys
import cv2
import time
import numpy as np
import datetime
import csv
from csv import DictReader
import pandas as pd
import time
from PIL import ImageTk, Image
window = tk.Tk()  
window.title("Register")
window.geometry('1500x800')
window.configure(background ='blue')

img5 =Image.open('log.jpg')
bg2 = ImageTk.PhotoImage(img5)
label7 = Label(window, image=bg2)
label7.place(x = 0,y = 0)    
####    login_screen.geometry("1500x850")
##window.grid_rowconfigure(0, weight = 1) 
##window.grid_columnconfigure(0, weight = 1)
from tkinter import *
from tkinter import ttk

  
lbl = tk.Label(window, text = "ID No.",  
width = 10, height = 2, fg ="Black",  
bg = "#a4ba88", font = ('times', 25, ' bold ') )  
lbl.place(x = 450, y = 100) 
  
txt = tk.Entry(window,  
width = 10, bg ="white",  
fg ="green", font = ('times', 45, ' bold ')) 
txt.place(x = 750, y = 100) 
  
lbl2 = tk.Label(window, text ="Name",  
width = 10, fg ="Black", bg ="#a4ba88",  
height = 2, font =('times', 25, ' bold '))  
lbl2.place(x = 450, y = 200) 
  
txt2 = tk.Entry(window, width = 10,  
bg ="white", fg ="Black",  
font = ('times', 45, ' bold ')  ) 
txt2.place(x = 750, y = 200)


def TakeImages():
    id=(txt.get())
    name =(txt2.get()) 
    os.makedirs('dataset', exist_ok=True)  # face samples are saved here
    vid_cam = cv2.VideoCapture(0)
    face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    count=0
    while True:
        _, image_frame=vid_cam.read()
        gray=cv2.cvtColor(image_frame,cv2.COLOR_BGR2GRAY)
        faces=face_detector.detectMultiScale(gray, 1.3, 5)
        for(x,y,w,h)in faces:
            cv2.rectangle(image_frame,(x,y),(x+w,y+h),(255,0,0),2)
            count+=1
            print(count)
            cv2.putText(image_frame, str(count), (x,y-40), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)
            cv2.imwrite("dataset/User."+str(id)+'.'+str(count)+".jpg",gray[y:y+h,x:x+w])
            cv2.imshow('frame',image_frame)
        if cv2.waitKey(100)& 0xFF == ord('q'):
            #TrainImages()
            break
        elif count>120:
            break
    vid_cam.release()
    cv2.destroyAllWindows()
    res = "Images Saved for ID : " + id +" Name : "+ name
    row = [id, name]
    with open('UserDetails.csv', 'a+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
            
    csvFile.close() 
    #message.configure(text = res)
    TrainImages()


    ##os.system('face_datasets.py')
    
def TrainImages():
      # Import OpenCV2 for image processing
    # Import os for file path
    import cv2, os

    # Import numpy for matrix calculation
    import numpy as np

    # Import Python Image Library (PIL)
    from PIL import Image

    # Create Local Binary Patterns Histograms for face recognization
    #recognizer = cv2.face.createLBPHFaceRecognizer()

    recognizer = cv2.face.LBPHFaceRecognizer_create()


    # Using prebuilt frontal face training model, for face detection
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

    # Create method to get the images and label data
    def getImagesAndLabels(path):

        # Get all file path
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
        
        # Initialize empty face sample
        faceSamples=[]
        
        # Initialize empty id
        ids = []

        # Loop all the file path
        for imagePath in imagePaths:

            # Get the image and convert it to grayscale
            PIL_img = Image.open(imagePath).convert('L')

            # PIL image to numpy array
            img_numpy = np.array(PIL_img,'uint8')

            # Get the image id
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            print(id)

            # Get the face from the training images
            faces = detector.detectMultiScale(img_numpy)

            # Loop for each face, append to their respective ID
            for (x,y,w,h) in faces:

                # Add the image to face samples
                faceSamples.append(img_numpy[y:y+h,x:x+w])

                # Add the ID to IDs
                ids.append(id)

        # Pass the face array and IDs array
        return faceSamples,ids

    # Get the faces and IDs
    faces,ids = getImagesAndLabels('dataset')

    # Train the model using the faces and IDs
    recognizer.train(faces, np.array(ids))

    # Save the model into trainer.yml
    recognizer.write('trainer.yml')
    print("Training Done")
    register()
 


  
def register():
    root=Tk()
    root.geometry('150x50')
    root.title("Register")
    lbl=Label(root, text="Register Successful")
    
    lbl.pack()
    root.mainloop()
    
    
    
    

takeImg = tk.Button(window, text ="Submit", 
command = TakeImages, fg ="black", bg ="#a67c35",  
width = 7, height = 1, activebackground = "Red",  
font =('times', 25, ' bold ')) 
takeImg.place(x = 480, y = 300)


quitWindow = tk.Button(window, text ="Quit",
command = window.destroy, fg ="black", bg ="#a67c35",  
width = 7, height = 1, activebackground = "Red",  
font =('times', 25, ' bold ')) 
quitWindow.place(x = 800, y = 300)

#label.pack()
window.mainloop() 
  
