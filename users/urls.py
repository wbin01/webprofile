from django.urls import path
from .views import *

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('signup', signup, name='signup'),
    path('signup', signup, name='signup'),
    path('<str:username>', dashboard, name='dashboard'),
    path('<str:username>/draft', dashboard_draft, name='dashboard_draft'),
    path('<str:username>/settings', settings, name='settings'),
]
