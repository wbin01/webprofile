from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('content', content, name='content'),
    path('create', create, name='create'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('signup', signup, name='signup'),
]
