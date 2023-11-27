
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username already exists")
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            return HttpResponse("Passwords do not match")

    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return HttpResponse("Invalid login credentials")

    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login') 