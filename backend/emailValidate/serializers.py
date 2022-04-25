from emailValidate.models import EmailValid
from rest_framework import serializers
# from django.core.mail import send_mail


class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmailValid
        fields = ('value', 'email_address', 'time')
