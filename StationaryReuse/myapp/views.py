from django.shortcuts import render
from myapp.forms import UserLoginModelForm, UserRegistrationModelForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.models import User

# Create your views here.

def UserLoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponse("user Logged In Successfully")
        else:
            return HttpResponse("YOU MADE A BLUNDER")
    else:
        return render(request, 'myapp/UserLogin.html')


def UserRegistrationView(request):
    if request.method=="POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password == confirm_password:
            user = User.objects.create(username=username, email=email, password=password)
            user.set_password(user.password)
            user.save()
            return HttpResponse("USER REGISTRATION SUCCESSFUL")
        else:
            return HttpResponse("INVALID CREDENTIALS!")
    else:
        return render(request, 'myapp/UserRegistration.html')


