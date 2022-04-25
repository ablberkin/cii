from django.db import models
# 导入内建的User模型。
from django.contrib.auth.models import AbstractUser
# timezone 用于处理时间相关事务。
from django.utils import timezone
from django.conf import settings
# 博客文章数据模型
import users.models
from ckeditor_uploader.fields import RichTextUploadingField


class ArticlePost(models.Model):
    # 文章作者。参数 on_delete 用于指定数据删除的方式，避免两个关联表的数据不一致。
    author = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, verbose_name="作者")

    category = models.CharField(max_length=20, choices=(("collegeNews", u"学院讯息"), ("academiaNews", "学术"),
                                                        ("lifeNews", "生活"), ("partyNews", "党")), default="collegeNews",
                                verbose_name="消息种类")

    # django 在每一次save()操作后都可以正常的增加一条数据并且id顺序自增
    id = models.AutoField(primary_key=True)

    # 文章标题。models.CharField 为字符串字段，用于保存较短的字符串，比如标题
    title = models.CharField(max_length=100, verbose_name="标题")
    introduction = models.CharField(max_length=40, verbose_name="介绍", null=True)
    # 文章正文。保存大量文本使用 TextField
    body = RichTextUploadingField (verbose_name="正文")

    # 文章创建时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)

    # 文章更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title
