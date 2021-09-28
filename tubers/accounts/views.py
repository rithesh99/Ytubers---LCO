from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Sign in success')
            return redirect('dashboard')
        else:
            messages.success(request, 'Invalid credentials')
            return redirect('signin')

    return render(request, 'accounts/signin.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if not(firstname) or not(lastname) or not(username) or not(email) or not(password): 
            messages.error(request,'Please enter valid details')
            return redirect('signup')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email already exists')
                return redirect('signup')

            user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('signin')
                
        else:
            messages.error(request, 'Password do not match')
            return redirect('signup')

    return render(request, 'accounts/signup.html')

def logout_user(request):
    logout(request)
    return redirect('signin')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

