from newsindex.models import ArticlePost
from rest_framework import serializers


class newsindexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArticlePost
        fields = ('author', 'category', 'id', 'title', 'introduction', 'body', 'created', 'updated')



