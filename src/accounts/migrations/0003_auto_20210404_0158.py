# Generated by Django 3.1.7 on 2021-04-04 01:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210404_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='name', max_length=60, verbose_name='Nome'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='nick',
            field=models.CharField(default='nick', max_length=20, verbose_name='Nome'),
            preserve_default=False,
        ),
    ]
