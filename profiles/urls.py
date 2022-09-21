from django.urls import path
from profiles.views import *


urlpatterns = [
    path('update_cover_image', update_cover_image, name='update_cover_image'),
    path('update_profile_image', update_profile_image,
         name='update_profile_image'),
]
