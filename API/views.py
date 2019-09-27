from django.shortcuts import render
from rest_framework import generics
from API.serializer import *
from blog.models import UserProfile, Post
from API.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser


#Пользователи
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = (IsOwnerOrReadOnly, )

class UserListView(generics.ListAPIView):
    serializer_class = UserDetailSerializer
    queryset = UserProfile.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )

class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    queryset = UserProfile.objects.all()


#Мероприятия
class PostCreateView(generics.CreateAPIView):
    serializer_class = PostDetailSerializer

class PostListView(generics.ListAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()

class PostDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()