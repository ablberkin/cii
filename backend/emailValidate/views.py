import datetime
import time
from random import random

from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.shortcuts import render, redirect
import emailValidate.models
from django.shortcuts import render
from django.conf import settings

# Create your views here.
from rest_framework import viewsets
from emailValidate.serializers import EmailSerializer
from emailValidate.models import EmailValid
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail


class EmailViewSet(viewsets.ModelViewSet):
    """
    查看，编辑博客的API接口
    """
    queryset = EmailValid.objects.all()
    serializer_class = EmailSerializer


def random_str():
    _str = '1234567890abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(_str) for i in range(4))


@api_view(['POST'])
def sendEmail(request):  # 获取全部数据
    result = {'state': ''}
    email_name = [request.data.get('email_address')]
    code = request.data.get('value')
    # email_name = post
    if request.method == 'POST':
        subject = 'cii验证码'  # 主题
        text_content = str('验证码为：') + str(code)
        print(request.data.get('email_address'))
        send_mail(subject, text_content, settings.EMAIL_FROM, email_name) #正式使用时打开
        # msg = EmailMultiAlternatives(subject, text_content, '369565049@qq.com', [email_name])
        # msg.send()  # 发送
        result['state'] = 'success'
        return JsonResponse(result)

@api_view(['GET'])
def emailvalidSearch(request):  # 根据email查找验证码
    email_address = request.GET.get('email_address')
    if id is not None:
        users = EmailValid.objects.filter(email_address=email_address).order_by('-id')
        # users = users.reverse()
        users = users[0: 1]
        serializer = EmailSerializer(users, many=True)

        return Response(serializer.data)
    else:
        return Response(str('请传email'))

# def send_message(request):
#     result = {'state': 'error', 'data': ''}
#     if request.method == 'GET':
#         # 1.获取邮箱
#         email_name = request.GET.get('email')
#         if email_name:
#             # 2.向邮箱发送邮件
#             try:
#                 subject = '全球水果生鲜系统发送的验证码'  # 主题
#                 yzm = random_str()  # 验证码
#                 text_content = '您好,您的验证码为:%s ,打死也不要告诉别人!!!' % yzm  # 内容
#                 html_content = """
#                     <div>
#                         <p>
#                             您好,您的验证码为:%s ,打死也不要告诉别人!!!
#                         </p>
#                     </div>
#
#                 """ % yzm  # html类型
#                 msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_FROM, [email_name])
#                 # msg.attach_alternative(html_content, 'text/html')  # 发送html 内容
#                 msg.send()  # 发送
#             except Exception as e:
#                 result['data'] = str(e)
#             else:
#                 """将内容保存到数据库"""
#                 result['data'] = 'success'
#                 result['state'] = 'success'
#                 # 保存到数据库
#                 email_valid = emailValidate.models.EmailValid()
#                 email_valid.value = yzm  # 验证码
#                 email_valid.email_address = email_name  # 邮箱名称
#                 email_valid.time = datetime.datetime.now()  # 时间戳
#                 email_valid.save()
#
#             finally:
#                 # 3.保存到数据库
#                 return JsonResponse(result)
#
#     # 如果没有进入if，就重定向到 邮箱注册页面
#     return redirect('/buyer/register_email/')
#
# #邮箱注册
# def register_email(request):
#     error_msg = {}
#     if request.method == 'POST':
#         # 先校验 在保存
#         # 1.获取表单提交过来的内容
#         email_name = request.POST.get('emailname')  # 邮箱名称
#         yzm = request.POST.get('code')  # 验证码
#         userpass = request.POST.get('userpass')  # 密码
#         # 2.去数据库中查询内容
#         email_obj = emailValidate.models.EmailValid.objects.filter(email_address=email_name).last()  # 获取最新的
#         # 判断邮箱是否存在
#         if email_obj:
#             # 3.判断
#             if email_obj.value == yzm:
#                 # 判断时间是否在有效范围内
#                 db_time = time.mktime(email_obj.time.timetuple())  # 数据库时间
#                 now_time = time.mktime(datetime.datetime.now().timetuple())  # 当前时间
#                 if now_time - db_time < 180000:  # 3分钟有效
#                     # 1.将用户名和密码保存到数据库
#                     buyer_obj = emailValidate.models.Buyer()
#                     buyer_obj.name = email_name
#                     buyer_obj.password = userpass  # 对密码进行加密
#                     buyer_obj.save()
#                     # 2.删除验证码
#                     email_obj.delete()
#                     # 3.重定向到登录界面
#                     return redirect('/buyer/login/')
#                 else:
#                     """验证码失效"""
#                     error_msg['yzm_sx'] = '验证码失效'
#                     # 删除数据库中的验证码
#                     email_obj.delete()
#             else:
#                 """验证码不正确"""
#                 error_msg['yzm_error'] = '输入的验证码不正确'
#         else:
#             """邮箱不存在"""
#             error_msg['email'] = '邮箱不存在'
#
#     return render(request, 'buyer/register_email.html', {'error_msg': error_msg})


# Create your views here.
