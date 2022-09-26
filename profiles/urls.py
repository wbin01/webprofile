from django.urls import path
from profiles.views import *


urlpatterns = [
    path('update_cover_image', update_cover_image, name='update_cover_image'),
    path('clear_cover_image', clear_cover_image, name='clear_cover_image'),

    path('update_profile_image', update_profile_image,
         name='update_profile_image'),
    path('clear_profile_image', clear_profile_image,
         name='clear_profile_image'),
]
