from django.contrib import admin 
from django.urls import path, include
from API.views import *


app_name = 'API'
urlpatterns = [
    path('acc/create/', UserCreateView.as_view()), #редактирование пользователя
    path('acc/getlist/', UserListView.as_view()), #список всех пользователей
    path('acc/detail/<int:pk>', UserDetailView.as_view()), #доступ к пользователю по id
    path('post/create/', PostCreateView.as_view()), #редактирование мероприятия
    path('post/getlist/', PostListView.as_view()), #список всех мероприятий 
    path('post/detail/<int:pk>', PostDetailView.as_view()), #доступ к пользователю по id
]
