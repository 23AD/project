from django.shortcuts import render
import pyautogui


# Create your views here.

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        from django .contrib import auth
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            from .models import uploads
            Expert = uploads.objects.all()
            return render(request, 'login.html', {'Expert': Expert})
        else:
            pyautogui.alert("Wrong Username or Password")
            return render(request, 'login.html')
