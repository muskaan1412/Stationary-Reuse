from django.conf.urls import include
from django.urls import path
from myapp import views

app_name = 'user'

urlpatterns = [
    path('<str:username>', views.UserProfileView, name="profile")
]