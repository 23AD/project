from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import pyautogui as pu


# Create your views here.

def Register(request, self=None):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            pu.alert("Username already exit")
            return render(request, 'register.html')
        else:
            user = User.objects.create_user(firstname=firstname, lastname=lastname, username=username, email=email,
                                            phone=phone, password=password)
            user.save()
            # print("user created")
            pu.confirm("User created")
            return redirect('/')
    else:
        return render(request, 'register.html')
