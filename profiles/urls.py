from django.urls import path
from profiles.views import *


urlpatterns = [
    path('update_cover_image/sender:<str:url_to_go_back>/user:<str:url_username>',
         update_cover_image, name='update_cover_image'),
    path('clear_cover_image/sender:<str:url_to_go_back>/user:<str:url_username>',
         clear_cover_image, name='clear_cover_image'),
    path('update_profile_image/sender:<str:url_to_go_back>/user:<str:url_username>',
         update_profile_image, name='update_profile_image'),
    path('clear_profile_image/sender:<str:url_to_go_back>/user:<str:url_username>',
         clear_profile_image, name='clear_profile_image'),
]
