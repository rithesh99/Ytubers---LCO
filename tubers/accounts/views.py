from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def signin(request):
    return render(request, 'accounts/signin.html')

def signup(request):
    return render(request, 'accounts/signup.html')

def logout_user(request):
    logout(request)
    return redirect('signin')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

