from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy

# Create your views here.
def register(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        comfirm_password = req.POST['confirm_password']
        email = req.POST['email']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']

        if password != confirm_password:
            message.error(req, "Password do not match")
        elif User.objects.filter(username=username).exists():
            message.error(req, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            message.error(req, "Email already exists")
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            messages.success(req, "User created successfully!")
            login(req, user)
            return redirect('login')

    return render(req, 'register.html')

class UserLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('post_list')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')