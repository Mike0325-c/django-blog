from django.db import models


# Create your models here.
class User(models.Model):

    id = models.AutoField(primary_key=True)
    # verbose_name 就是解释的作用
    username = models.CharField(max_length=32, verbose_name='用户名')
    # ver_name是用来给该字段添加说明的

    password = models.IntegerField()
    info = models.CharField(max_length=32, default='111')
    hobby = models.CharField(max_length=32, null = True)

    def __str__(self):
        return self.username


class Userjjy(models.Model):

    id = models.AutoField(primary_key=True)
    username123123 = models.CharField(max_length=32, verbose_name='用户名')
    # ver_name是用来给该字段添加说明的
    password = models.IntegerField()
    info = models.CharField(max_length=32, default='111')
    hobby = models.CharField(max_length=32, null = True)