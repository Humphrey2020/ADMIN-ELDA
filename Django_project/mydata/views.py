from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from  ed import settings
from django.core.mail import send_mail
def index(request):
      return render(request,'index.html')

def signup(request):
        
        if request.method=="POST":   #  Response 
               username=request.POST['username']
               fname=request.POST['fname']
               lname=request.POST['lname']
               email=request.POST['email']
               pass1=request.POST['pass1']
               pass2=request.POST['pass2']
               if User.objects.filter(username=username):
                      messages.error(request,'username already exit ,please try some other username') 
                      return redirect('index')
               if User.objects.filter(email=email):
                      messages.error(request,'Email already exit') 
                      return redirect('index') 
               if len(username)>10:
                      messages.error(request,'username must be under 10')
               if pass1 !=pass2:
                      messages.error(request,'password do not match') 
               if  not username.isalnum():
                      messages.error(request, 'username must be alpha numeric')
                      return redirect('index')
               myuser=User.objects.create_user(username,email,pass1)
               myuser.first_name=fname
               myuser.last_name=lname
               myuser.save()
               
               messages.success(request,'your Account as been saved successfully created we have sent a confimation email please confirma your email in order to activate your account ')

               # welcome email 
               subject='welcome to Elda tutor' 
               message ='hello' + myuser.first_name + '!! \n' + 'weclome to grg !! \n thank you for visiting our website \n we have also sent  you a confirmation email please confirm your email addresss in order to activate your account . \n\n Thank you \n humphey'
               from_email=settings.EMAIL_HOST_USER 
               to_list=[myuser.email] 
               send_mail(subject,message,from_email,to_list,fail_silently=True)
               
               return redirect('signin')
        
        return render(request, 'signup.html')


def signin(request):
       if request.method=="POST":
               username=request.POST['username']
               pass1=request.POST['pass1']
               user=authenticate(username=username,password=pass1)
               if user is not None:
                      login(request,user)
                      fname=user.first_name
                      return render(request,'index.html',{'fname':fname})
               else:
                      messages.error(request,'bad credential')
                      return redirect('index')
       return render(request, 'signin.html') 
   

def signout(request):
       logout(request)
       messages.success(request,"logged out succesfully")
       return redirect('index')

