from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('content/<int:post_id>', content, name='content'),
    path('create', create, name='create'),
    path('edit/<int:post_id>', edit, name='edit'),
    path('update/<int:post_id>', update, name='update'),
    path('delete/<int:post_id>', delete, name='delete'),
    path('testview', testview, name='testview'),
]
