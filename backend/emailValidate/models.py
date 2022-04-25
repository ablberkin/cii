from django.db import models


class EmailValid(models.Model):
    value = models.CharField(max_length=32)  # 保存验证码
    email_address = models.CharField(max_length=32)  # 邮箱名称
    time = models.DateTimeField()  # 时间戳

