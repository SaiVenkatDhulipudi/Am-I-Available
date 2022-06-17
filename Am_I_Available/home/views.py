from django.shortcuts import render,HttpResponse
def home(request):
    return HttpResponse(request,"hello")
def Faculty_registration(request):
    if request.method=="POST":
        return HttpResponse(request,"<h1>registration success</h1>")
    else:
        return render(request,'Faculty_registration.html')