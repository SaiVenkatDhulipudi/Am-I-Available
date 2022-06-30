from django.shortcuts import render
from django.http import FileResponse,HttpResponse
import pyrebase
from PIL import Image, ImageFont, ImageDraw
from collections import defaultdict
import qrcode
from cryptography.fernet import Fernet
import PIL
class branch:
    def __init__(self) -> None:
        self.departments=defaultdict(lambda:'')
        self.departments['CSE']="11"
        self.departments['CIVIL']="12"
        self.departments['MECH']="13"
        self.departments['AIDS']="14"
        self.departments['ECE']="15"
        self.departments['EEE']="16"
        self.departments['BS&H']="17"
        self.departments['TP']="18"
        self.departments['EC']="19"
        self.departments['ECM']="20"
        self.departments['IT']="21"
        self.departments['Principal']="10101"
        self.departments['Rector']="10202"
        self.departments['CEO']="10303"

class IDmaker:
    def __init__(self,data) -> None:
        my_image = Image.open("static/img/ID.jpg")
        paste_image=Image.open("static/img/{}.jpg".format(data["ID"]))
        paste_image=paste_image.resize((1090,1090))
        my_image.paste(paste_image,(500,700))
        title_font = ImageFont.truetype('static/fonts/BebasNeue-Regular.ttf',120)
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((780,2050),data["ID"], (0, 0,0), font=title_font)
        image_editable.text((780,2200),data['name'], (0, 0,0), font=title_font)
        image_editable.text((780,2350),data['dept'], (0, 0,0), font=title_font)
        image_editable.text((780,2500),data['designation'], (0, 0,0), font=title_font)
        image_editable.text((780,2650),data["phNo"], (0, 0,0), font=title_font)
        my_image.save("static/img/{}.jpg".format(data["ID"]))

class helper():
    def __init__(self):
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
        self.auth = firebase.auth()
        self.db=firebase.database()
    def qrgen(self,data):
        def encry(data):
            key="T700BpRe9R98gb7CRdi_i5R7TN3-tx3-OeG5ea2wEr0=".encode()
            fernet = Fernet(key)
            encrypted = fernet.encrypt(data.encode())
            return encrypted
        qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4,)
        qr.make(fit=True)
        pat="static/img/{}.jpg".format(data)
        data=encry(data)
        qr.add_data(data)
        img = qr.make_image() 
        img.save(pat)
def login(request):
    if request.method=="POST":
        email=request.POST["email"]
        passw=request.POST["pass1"]
        try:
            help=helper()
            auth=help.auth
            user=auth.sign_in_with_email_and_password(email,passw)
            print(user)
            # request.set_cookie("sessionid",user['idToken'])
            return render(request,"index.html")
        except:
            return render(request,"login.html",{"message":"Enter vaild Credentials"})
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")
def home1(request):
    return render(request,"index.html")
def Faculty_registration(request):
    if request.method=="POST":
        data=defaultdict(lambda:0)
        help=helper()
        auth=help.auth
        db=help.db
        email=request.POST["email"]
        password=request.POST["pass1"]
        user=auth.create_user_with_email_and_password(email, password)
        auth.send_email_verification(user['localId'])
        branc=branch()
        x=(db.child("faculty").child(request.POST["dept"])).get()
        x=x.val()
        data["ID"]=branc.departments.get(request.POST["dept"])+str(101+len(x))
        data['name']= request.POST["Prefered_Name"] 
        data['dept']=request.POST["dept"]
        data['designation']=request.POST["designation"]
        data["phNo"]=request.POST["contact"]
        data["first_name"]=request.POST["first_name"]
        data["first_name"]=request.POST["surname"]
        data["address"]=request.POST["address"]
        data["email"]=request.POST["email"]
        db.child("faculty").child(request.POST["dept"]).child(data["ID"]).set(data)
        db.child("status").child(data["ID"]).set(0)
        help.qrgen(data["ID"])
        id=IDmaker(data)
        return send_file(request,data["ID"])
    else:
        return render(request,'Faculty_registration.html')

def send_file(response,ID):

    img = open('static/img/{}.jpg'.format(ID), 'rb')
    response = FileResponse(img)
    return response