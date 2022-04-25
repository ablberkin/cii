from django.db import models


# Create your models here.
class Img(models.Model):
    img = models.ImageField(max_length=1000, upload_to='image/%Y/%m/', verbose_name=u'头像', null=True, blank=True)
