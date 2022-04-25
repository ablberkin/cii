from rest_framework.permissions import IsAuthenticated

from users.models import UsersProfile
from rest_framework import serializers
# from itsdangerous import TimedJSONWebSignatureSerializer as ts
# from django.conf import settings
# from django.core.mail import send_mail
# from rest_framework import generics
from django.core.mail import send_mail


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsersProfile
        fields = ('id', 'name', 'username',  'gender', 'mobile', 'password', 'identity', 'email', 'collection')


# class EmailSendSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UsersProfile
#         fields = ('id', 'email')
#
#     def validate(self, attrs):
#         return attrs
#
#     def update(self, instance, validated_data):
#         # instance是从数据库查询出的对象
#         instance.email = validated_data['email']
#         # 这里更新一次email字段数据
#         instance.save()
#         # 创建一个isdangerous的对象，传入我们设置中的密钥
#         idsfy = ts(settings.SECRET_KEY)
#         print(idsfy)
#         data = {
#             'user_id': instance.id,
#             'username': instance.username,
#             'email': instance.email,
#         }
#         # 生成isdangerous token
#         token = idsfy.dumps(data).decode()
#         # 拼接路径
#         url = 'http://127.0.0.1:8000/email/vary/?token=' + token
#         # 拼接邮件内容
#         url_str = '<a href=' + url + '>click to verify ur email</a>'
#         print(instance)
#         email_url = validated_data['email']
#         print(email_url)
#         # 发送验证邮件
#         send_mail(subject='hermit email active', message=url_str, from_email=settings.EMAIL_FROM,
#                   recipient_list=[email_url], html_message=url_str)
#
#         return instance
#
#
# class EmailSendView(generics.UpdateAPIView):
#     serializer_class = serializers.EmailSendSerializer
#     permission_classes = (IsAuthenticated,)
#
#     def get_object(self):
#         return self.request.user