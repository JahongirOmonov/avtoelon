from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, generics
from avto.models import Post, Account
from avto.serializers import PostSerializer, AccountSerializer


# Create your views here.
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AccountCreate(generics.CreateAPIView):
    queryset=Account
    serializer_class=AccountSerializer
