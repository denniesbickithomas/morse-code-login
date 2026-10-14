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
####import attachem
####from twilio.rest import Client
####from playsound import playsound



from tkinter import *
from tkinter import ttk
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX
df=pd.read_csv("UserDetails.csv")
cam = cv2.VideoCapture(0)

flag = []
count1=0
count2=0
count3=0
sample =0
lecture=0
mon=0
count=0
var2=0
var=0
t=0
var1=0
def successful():
    root=Tk()
    root.geometry('250x150')
    root.configure(background ='#a2f59f')
    root.title("Success")
    lbl=Label(root, text="Logged In Successfully",bg ='#a2f59f')
    print("Login Successful1111")   
    lbl.pack()
##    quitWindow = tk.Button(root, text ="OK",  
##    command = root.destroy, fg ="white", bg ="blue",  
##    width = 5, height = 1, activebackground = "Red",  
##    font =('times', 15, ' bold ')) 
##    quitWindow.place(x = 85, y = 50)
    #time.sleep(1)

    root.mainloop()
   # root.destroy()

def unsuccessful():
    root=Tk()
    root.geometry('150x50')
    root.title("UnSuccess")
    root.configure(background ='#e3684f')
    lbl=Label(root, text="Logged In UnSuccessful",bg ='#e3684f')
    print("Login unSuccessful") 
    #cam.release()
    #cv2.destroyAllWindows()
    #window.destroy()
    lbl.pack()
    root.mainloop()

while True:
    now = datetime.datetime.now()
    ret, im =cam.read()
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2,5)
    if t==1:
        t=0
        break
    
    for(x,y,w,h) in faces:
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
        Id,i = recognizer.predict(gray[y:y+h,x:x+w])

        print(i)  ##successful
        if i < 55:
            aa=df.loc[df['Id'] == Id]['name'].values
            tt=str(Id)+"-"+aa
            Id = df.loc[df['Id']== Id] ['name'].values
            #print("known")
            var1=1
##                if True:
            #successful()
           # print('known')
        else:
            count=count+1
            Id = "unknown"
            #tt=str(Id)

            if count > 10:
                count=0
            Id="unknown"
            print("unknown")
            cv2.imwrite("frame.png",im)
########            client.api.account.messages.create(
########                to="<YOUR_PHONE_NUMBER>",
########                from_="<YOUR_TWILIO_NUMBER>",
########                body=" Unknown Detected" )
########            print("Msg Sent")
########            
########            attachem.sendMail( ["<RECIPIENT_EMAIL>"],
########                      "Section b attendance",
########                      "this is the body text of the email",
########                      ["frame.png"] )
            print("mail Sent")
##            playsound("2.mp3")
            time.sleep(5)
            
               # tt=str(Id)
            mon=0
            var2=1
                      

        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)

    cv2.imshow('im',im)
    
    if var2==1 and count > 5:
        var2=0
        print("unsuccess")
        #var1=0
        unsuccessful()
        t=1
        cam.release()
        cv2.destroyAllWindows()
        break

    elif var1==1:
        var1=0
        print("Success")
        successful()
        t=1
        cam.release()
        cv2.destroyAllWindows()
        break


    if cv2.waitKey(20) & 0xFF == ord('q'):
        break



cam.release()
cv2.destroyAllWindows()
     

        
#window.mainloop() 
  
