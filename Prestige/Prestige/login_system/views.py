from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def signup(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']    
        gender = request.POST['gender']
        phone = request.POST['phone']

        if password1 == password2:
        
            if User.objects.filter(username = username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
        
            elif User.objects.filter(email = email).exists():
                print('username already taken')
                messages.info(request,'email already registered')
                return redirect('signup')
        
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name = last_name, is_staff = False, is_admin = False)

                user.save();
                
                print('user created')
                return redirect('login_system:login')
        
        else:
            print('password not matching...')
            messages.info(request,'Password does not match')
            return redirect('register')

        return redirect('/')
    else:
        return render(request, 'signup.html')


def login(request, next = "/account/customer"):
    if request.method == 'POST':
        username = request.POST['username']
        
        password = request.POST['password1']      
        user = auth.authenticate(username=username,password = password)  

        if user is not None:
            auth.login(request,user)
            return redirect(next)
        else:
            messages.info(request,'invalid credentials')
            return redirect('login_system:login')
    
    if request.method == 'GET':
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')