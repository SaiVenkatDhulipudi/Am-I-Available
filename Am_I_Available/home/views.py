from django.shortcuts import render
from django.http import FileResponse,HttpResponse
import requests
def home1(request):
    return HttpResponse("Welcome")
def Faculty_registration(request):
    if request.method=="POST":
        return send_file(request)
    else:
        return render(request,'Faculty_registration.html')

def send_file(response):

    img = open('static/img/result.jpg', 'rb')
    response = FileResponse(img)
    return response