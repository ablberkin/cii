from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from blogapp.serializers import BlogSerializer
from blogapp.models import Blog


class BlogViewSet(viewsets.ModelViewSet):
    """
    查看，编辑博客的API接口
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
