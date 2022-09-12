from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('content', content, name='content'),
    path('create', create, name='create'),
]
