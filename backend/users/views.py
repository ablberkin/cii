import random

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# from __future__ import unicode_literals

from rest_framework import viewsets, mixins
# from rest_framework.generics import UpdateAPIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import serializers

from users.serializers import UsersSerializer
from users.models import UsersProfile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings


# 随机数函数
# def random_str():
#     _str = '1234567890abcdefghijklmnopqrstuvwxyz'
#     return ''.join(random.choice(_str) for i in range(4))
#
#
# def email_send(request):
#     return render(request, 'email_send.html')
#
#
# def send_email(request):
#     """
#     邮件发送函数。ajax发送get请求，调用随机字符串函数，生成四位随机数，保存到session中，
#     并发送邮件到验证邮箱。
#     post请求中判断得到的随机字符串是否与session中所保存的字符串相同，若相同则重定向到主页面。
#     :param request:
#     :return:
#     """
#     if request.method == 'GET':
#         try:
#             email = request.GET['email']
#         except:
#             email = ''
#         email_code = random_str()
#         msg = '验证码：' + email_code
#         send_mail('邮箱验证', msg, settings.EMAIL_FROM,
#                   [email])
#         print(email_code)
#         # 将验证码保存到session中在接下来的操作中进行验证
#         request.session['email_code'] = email_code
#         return HttpResponse('ok')
#     else:
#         # 验证验证码是否输入正确
#         if request.POST.get('email_code') == request.session['email_code']:
#             print('正确')
#         else:
#             return HttpResponse('验证码错误')



@api_view(['GET'])
def getlist(request):  # 获取全部数据
    if request.method == 'GET':
        users = UsersProfile.objects.values('id', 'name', 'username', 'gender', 'mobile', 'password', 'identity',
                                            'email', 'collection').distinct()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def userSearch(request):  # 根据email查找单条数据
    email = request.GET.get('email')
    if id is not None:
        users = UsersProfile.objects.filter(email=email)
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response(str('请传email'))


class UsersViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.CreateModelMixin,
                   # viewsets.ModelViewSet
                   viewsets.GenericViewSet):
    """
    查看，编辑博客的API接口
    """
    queryset = UsersProfile.objects.all()
    serializer_class = UsersSerializer


# class EmailSendView(UpdateAPIView):
#     serializer_class = serializers.EmailSendSerializer
#     permission_classes = (IsAuthenticated,)
#     def get_object(self):
#         return self.request.user