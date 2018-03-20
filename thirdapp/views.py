from django.shortcuts import render
from thirdapp import forms
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from thirdapp.models import UserProfileInfo
# Create your views here.
def index(request):
    return render(request,"thirdapp/index.html")

def register(request):
    register=False
    if request.method=='POST':
        user_form=forms.UserForm(request.POST)
        profile_form=forms.UserProfile(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            register=True

    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfile()
    return render(request,'thirdapp/register.html',{'user_form':user_form,'profile_form':profile_form,'register':register})

def Login(request):
    if request.method=='POST':
        login_form=forms.Login(request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            user=authenticate(username=username, password=password)
            if user:
                login(request,user)
                request.session['username']=username
                return HttpResponseRedirect(reverse('thirdapp:index'))
            else:
                return HttpResponse("Invalid Login Details")

    else:
        login_form=forms.Login()
    return render(request,'thirdapp/login.html',{'login_form':login_form})

@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('thirdapp:index'))

@login_required
def user_detail(request):
    if request.session['username']:
        user=User.objects.get(username=request.session['username'])
        #user_profile=UserProfileInfo.objects.get(user=user)
    else:
        print("login again your session has been expired")

    return render(request,'thirdapp/user_detail.html',{'user':user})