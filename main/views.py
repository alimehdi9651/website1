from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return render(request, 'index.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user:
             login(request, user)
             return redirect('index')
             
    return render(request, 'login.html')
def register_view(request):
         if request.method == 'POST':
              username = request.POST.get('username')
              password = request.POST.get('password')
              email = request.POST.get('email')
              confirmpassword = request.POST.get('confirmpassword')
              print(username, email,password, confirmpassword)
              if password == confirmpassword:
                   user = User(username = username, email= email)
                   user.set_password(password)
                   user.save()
                   return redirect('login')
            
         return render(request, 'register.html')
def logout_view(request):
     logout(request)
     return redirect('index')
     
 