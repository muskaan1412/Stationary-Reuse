from django.contrib import admin
from myapp.models import UserInfoModel, AdsInfoModel, AdsPhotosModel, FavouriteAdsModel

# Register your models here.

admin.site.register(UserInfoModel)
admin.site.register(AdsInfoModel)
admin.site.register(AdsPhotosModel)
admin.site.register(FavouriteAdsModel)
