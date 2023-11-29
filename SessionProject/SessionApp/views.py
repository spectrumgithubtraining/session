from django.shortcuts import render,redirect
from django.http import HttpResponse
# from.models import Form
from django.contrib.auth.models import User
from django.contrib import messages,auth
def index(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            user.save()
            return redirect('/reg')
        else:
            messages.info(request,"invalid")
            return redirect('/')
    return render(request,"login.html")

def reg(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        confirmPassword=request.POST['confirmPassword']
        #password verification
        if password == confirmPassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('/')
              
            elif User.objects.filter(password=confirmPassword).exists():
                messages.info(request,"password taken")
                return redirect('/')
              
            else:
                myuser=User.objects.create_user(username=username,password=password)
                myuser.save()  
                return redirect('/')
        else:
            messages.error(request,"password not match")
            return redirect("/")
    return render(request,"register.html")
# Create your views here.
