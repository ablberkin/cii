# Generated by Django 4.0.1 on 2022-03-27 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='image/%Y/%m/', verbose_name='头像'),
        ),
    ]
