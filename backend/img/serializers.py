from img.models import Img
from rest_framework import serializers


class ImgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Img
        fields = ('img')
