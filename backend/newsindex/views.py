# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from newsindex.serializers import newsindexSerializer
from newsindex.models import ArticlePost


class newsindexViewSet(viewsets.ModelViewSet):
    """
    查看，编辑博客的API接口
    """
    queryset = ArticlePost.objects.all()
    serializer_class = newsindexSerializer
