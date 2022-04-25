from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class UsersProfile(AbstractUser):
    """
    用户信息
    """
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    # 用户用手机注册，所以姓名，生日和邮箱可以为空
    name = models.CharField(max_length=30, null=True, verbose_name="姓名")
    # user_name = models.CharField("用户名", max_length=30, null=True, blank=False)
    # birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=10, choices=(("male", u"男"), ("female", "女")), default="female",
                              verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    password = models.CharField(max_length=100, null=True, blank=True, verbose_name="密码")
    identity = models.CharField(max_length=20,
                                choices=(("teacher", u"教职工"), ("student", "学生"), ('tourist', '游客')),
                                default="student",
                                verbose_name="身份")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    collection = models.CharField(null=True, blank=True, max_length=11, verbose_name="收藏")
    email_address = models.CharField(max_length=32, null=True)
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    验证码
    """
    code = models.CharField("验证码", max_length=10)
    email = models.CharField("邮箱", max_length=11)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
