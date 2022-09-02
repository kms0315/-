from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import User
from django.contrib.auth.hashers import check_password

# Create your views here.
def chpass(request):
    cp=request.POST.get("cpass")
    if check_password(cp,request.user.password):
        np=request.POST.get("npass")
        request.user.set_password(np)
        request.user.save()
        return redirect("acc:login")
    else:
        return redirect("acc:update")
def update(request):
    if request.method=="POST":
        u=request.user
        un=request.POST.get('umail')
        uc=request.POST.get('ucom')
        up=request.FILES.get('upic')
        u.comment,u.email=uc,un
        if up:
            u.pic.delete()
            u.pip.save()
        u.save()
        return redirect("acc:profile")
    return render(request,"acc/update.html")
def delete(request):
    u=request.user
    k=request.POST.get('ckpw')
    if check_password(k, u.password):
        u.pic.delete()
        u.delete()
        return redirect('acc:index')
    return redirect('acc:profile')
def userlogout(request):
    logout(request)
    return redirect('acc:index')
def profile(request):
    return render(request,'acc/profile.html')

def signup(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        up=request.POST.get('upass')
        uc=request.POST.get('ucom')
        pi=request.FILES.get('upic')
        try:
            User.objects.create_user(username=un,password=up,comment=uc,pic=pi)
            return redirect("acc:login")
        except:
            pass
    return render(request,"acc/signup.html")

def userlogin(request):
    if request.method=="POST":
        un=request.POST.get("user")
        pa=request.POST.get("pass")
        u=authenticate(username=un,password=pa)
        if u:
            login(request,u)
            return redirect("acc:index")
        else:
            pass #마지막 날
    return render(request,'acc/login.html')

def index(request):
    return render(request, 'acc/index.html')