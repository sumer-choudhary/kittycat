from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.messages.api import success
from django.shortcuts import render,redirect
from Info.models import Info
from .forms import Register,Login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.template import context




def index(request):
    return render(request,"index.html")

def contactme(request):
    return render(request,"contact-me.html")

def pricing(request):
    return render(request,"pricing.html")

def registration(request):
    fn=Register()
    dicts={"form":fn}
    return render(request,"registration.html",dicts)

def registerhandler(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        rpassword=request.POST.get("rpassword")
        if password == rpassword:
            if Info.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect ('registration')
            else:
                data=Info(name=name,email=email,password=password,rpassword=rpassword)
                data.save()
                messages.info(request,'User created!')
                return redirect('login')
        else:
            messages.info(request,'password not matching...')
            return redirect('registration')
        
        return redirect('/')
        
    else:
        return render(request,"registration.html")
   

def login(request):
    lg=Login()
    dt={"forms":lg}
    return render(request,"login.html",dt)

def loginhandler(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = Info.objects.all().filter(email=email, password=password)
        for values in user:
            if values.email == email and values.password == password:
                if user is not None:
                    print(email)
                    print(password)
                    messages.success(request,"Successfully Logged In")
                    return redirect('/')
                else: 
                    messages.error(request,"Invalid Credentials, please try again")
                    return redirect('login')
            else:
                messages.info(request,"invalid credentials")
                return render(request, 'registration.html')
    return HttpResponse('404 - Not found')          
            
def logouthandle(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "successfully logedout")
        return redirect("/")
   