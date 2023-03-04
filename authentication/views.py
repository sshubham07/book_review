#from readline import get_current_history_length
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from login_signup import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token 
from .models import *
import uuid
from . utils import *
#from django.utils.http import urlsafe_base64_decode


# Create your views here.
def home(request):
    return render(request, "authentication/index.html") 

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        c_password=request.POST['c_password']
        if User.objects.filter(username=username):
            messages.error(request, "User name already exits!!")
            return redirect('home')
        if User.objects.filter(email=email):
            messages.error(request, "Email already exits!!")
            return redirect('home')
        if password != c_password:
            messages.error(request, "Password did not match")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric")
            return redirect('home')
        my_user=User.objects.create_user(username,email, password)
        my_user.first_name=first_name
        my_user.last_name=last_name
        my_user.save()
        p_obj=Profile.objects.create(user=my_user,email_token=str(uuid.uuid4()))
        p_obj.save()
        send_mail_token(email,p_obj.email_token)
        messages.success(request, "Please verify your Email")
        return render(request, "home.html",{'f_name':username}) 
    return render(request, "authentication/signup.html")

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html',{'f_name':username})
        else:
            messages.error(request, "Error!! Somthing Went Wrong")
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')

def verify(request, token):
    try:
        obj=Profile.objects.get(email_token=token)
        obj.is_varified=True
        obj.save()
        return HttpResponse("YOUR ACCOUNT VERIFIED")
        
    except Exception as e:
        return HttpResponse("INVALID!!")
        

