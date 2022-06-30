from datetime import datetime
import cv2 as c
import numpy as np
import pyzbar.pyzbar as pyzbar
from cryptography.fernet import Fernet
import time
import pyrebase
import pyttsx3 as p
engine = p.init()
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)
engine.setProperty('rate', 178)
def speak(audio):
    print(f"{audio}")
    engine.say(audio)
    engine.runAndWait()
Config = {
    'apiKey': "AIzaSyBxIZPhs8tO7EjivqAv0B5dUd5VWfwvT3g",
    'authDomain': "miniproject-48f5c.firebaseapp.com",
    'databaseURL': "https://miniproject-48f5c-default-rtdb.firebaseio.com",
    'projectId': "miniproject-48f5c",
    'storageBucket': "miniproject-48f5c.appspot.com",
    'messagingSenderId': "934194697745",
    ' appId': "1:934194697745:web:20774e4e9de4890ca803b0",
    ' measurementId': "G-QC8HD1ZKVY"

    };

firebase= pyrebase.initialize_app(Config)
db=firebase.database()
#===========================================

key="T700BpRe9R98gb7CRdi_i5R7TN3-tx3-OeG5ea2wEr0=".encode()
fernet=Fernet(key)
def check(x):
    status=db.child("status").get()
    status=(status.val())
    for i in status:
        if i==x :
            return status[i]

def encry(data):
    decrypted=fernet.decrypt(data)
    return decrypted.decode()
if __name__=='__main__':
    cam=c.VideoCapture(0)
    coun=0
    while True:
        _, frame = cam.read()
        c.imshow('QR_DECODER',frame)
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            dat=obj.data
            x=(encry(dat))
            status=check(x)
            if status!=None:
                status=db.child("status").child(x).set(1 if status==0 else 0)
                speak("Authorised")
                exit()
        
        if  c.waitKey(1) & 0xFF == ord('q'):
            break
        coun+=1
    cam.release()
# Destroy all the windows
    c.destroyAllWindows()
    