from django.conf.urls import include
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'

urlpatterns = [
    path('<str:username>/', views.UserProfileView, name="profile"),
    path('<str:username>/editprofile/', views.UserEditProfileView, name="edit_profile")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)