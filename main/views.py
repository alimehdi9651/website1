from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import TaskForm
from .models import Task


def index(request):
    task_list = Task.objects.all() #select from tasks
    return render(request, 'index.html', {
         'task' : task_list,
         'form': TaskForm()
    })

def add_task(request):
     form = TaskForm(request.POST or None)
     if form.is_valid():
          form.save()
     return redirect('index')
     
def complete_task(request, id):
     task = Task.objects.get(id=id)
     task.completed = True
     task.save()
     return redirect('index')


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
     
 