from django.shortcuts import render
from myapp.forms import UserLoginModelForm, UserRegistrationModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.models import User
from myapp.models import UserInfoModel, AdsInfoModel, AdsPhotosModel, FavouriteAdsModel
from django.urls import reverse

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


def UserProfileView(request, username):
    user = User.objects.get(username=username)
    info = UserInfoModel.objects.get(user=user)
    var_dict = {"user": user, "info": info}
    return render(request, "myapp/profile.html", context=var_dict)


def UserEditProfileView(request, username):
    user = User.objects.get(username=username)
    info = UserInfoModel.objects.get(user=user)
    if request.method == "POST":
        name = str(request.POST.get("name"))
        print(name)
        if " " in name:
            user.first_name, user.last_name = name.split(" ")
            print(user.first_name, user.last_name)
        else:
            user.first_name = name
            user.last_name = ""
            print(user.first_name)
        user.email = request.POST.get("email")
        info.gender = request.POST.get("gender")
        info.college = request.POST.get("college")
        info.course = request.POST.get("course")
        info.description = request.POST.get("description")
        info.phone_number = request.POST.get("phone_number")
        info.address = request.POST.get("address")
        if "profile_pic" in request.FILES:
            info.profile_pic = request.FILES.get("profile_pic")
        user.save()
        info.save()
        return HttpResponseRedirect(reverse("user:profile", kwargs={"username":username}))
    else:
        var_dict = {"user":user, "info":info}
        return render(request, "myapp/edit_profile.html", context=var_dict)




