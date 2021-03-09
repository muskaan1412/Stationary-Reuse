from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfoModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="photos/userprofilepics", blank=True)
    description = models.CharField(max_length=250, blank=True)
    phone_number = models.PositiveSmallIntegerField()
    college = models.CharField(max_length=40, blank=True)
    branch = models.CharField(max_length=40, blank=True)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, default="Male", blank=True, null=True)
    
    def __str__(self):
        return self.user.username


class AdsInfoModel(models.Model):
    user = models.ForeignKey(UserInfoModel, on_delete=models.CASCADE, related_name="posted_ads")
    purpose = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    
    def __str__(self):
        return self.title


class AdsPhotosModel(models.Model):
    ads_info = models.ForeignKey(AdsInfoModel, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(upload_to="photos")


class FavouriteAdsModel(models.Model):
    user = models.ForeignKey(UserInfoModel, on_delete=models.CASCADE, related_name="favourite_ads")
    ad = models.OneToOneField(AdsInfoModel, on_delete=models.CASCADE)





