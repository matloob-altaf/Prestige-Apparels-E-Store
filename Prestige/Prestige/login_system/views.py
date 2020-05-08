from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from Guest.models import Customer, Orders
from django.urls import reverse

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
                messages.info(request,'Username Already Taken')
                return redirect('login_system:signup')
        
            elif User.objects.filter(email = email).exists():
                print('username already taken')
                messages.info(request,'Email already registered')
                return redirect('login_system:signup')
        
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name = last_name, is_staff = False, is_superuser = False)
                customer = Customer(user = user, phone_number = phone, address = "", gender = gender)
                customer.save()
                
                print('Customer created')
                messages.info(request,'Please Login to Continue')
                return redirect('login_system:login')
        
        else:
            print('password not matching...')
            messages.info(request,'Password does not match')
            return redirect('login_system:signup')

        return redirect('/')
    else:
        return render(request, 'signup.html')


def login(request, next = "/customer"):
    if request.method == 'POST':
        username = request.POST['username']
        
        password = request.POST['password1']      
        user = auth.authenticate(username=username,password = password)  
        
        if (user is not None):
            print("User Found")
            auth.login(request,user)

            cust = Customer.objects.filter(user = user).exists()

            if cust:
                print("Customer Found")
                return redirect('login_system:customer')
            else:
                return redirect('/')


        else:
            print("Customer Not Found")
            messages.info(request,'Invalid Credentials Or Customer Does Not Exist')
            return redirect('login_system:login')
    
    if request.method == 'GET':
        return render(request,'login.html')

def logout(request, next='/'):
    next1 = request.path
    auth.logout(request)
    next = request.META.get('HTTP_REFERER')
    return redirect(next)
    

def customerAccount(request):

    if (request.user.is_authenticated):
        cust = Customer.objects.filter(user = request.user).exists()
        print(cust)
        orders = Orders.objects.filter(customer = cust)
        return render(request,'customer.html',{'orders':orders})
    else:
        messages.info(request,'You need to login First')
        return redirect('login')

def cancelOrder(request):
    pass
