from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from blogapp.serializers import BlogSerializer
from img.models import Img
class ImgViewSet(viewsets.ModelViewSet):
    """
    查看，编辑博客的API接口
    """
    queryset = Img.objects.all()
    serializer_class = BlogSerializer
