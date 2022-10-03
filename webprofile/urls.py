from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('post/<str:url_title>:<int:post_id>', content, name='content'),
    path('create/sender:<str:url_to_go_back>', create, name='create'),
    path('edit/<str:url_title>:<int:post_id>/sender:<str:url_to_go_back>',
         edit, name='edit'),
    path('update/<int:post_id>', update, name='update'),
    path('delete/<str:url_to_go_back>:<int:post_id>', delete, name='delete'),
    path('search/post', search_post, name='search_post'),
    path('search/tag', search_tag, name='search_tag'),
    path('search/user', search_user, name='search_user'),
]
