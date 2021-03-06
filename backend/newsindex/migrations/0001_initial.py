# Generated by Django 4.0.1 on 2022-03-03 14:14

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePost',
            fields=[
                ('category', models.CharField(choices=[('collegeNews', '学院讯息'), ('academiaNews', '学术'), ('lifeNews', '生活'), ('partyNews', '党')], default='collegeNews', max_length=20, verbose_name='消息种类')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('introduction', models.CharField(max_length=40, null=True, verbose_name='介绍')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='正文')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
