from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=32)
    # 总共8位,小数点后两位123456.78
    price = models.DecimalField(max_digits=8, decimal_places=2)

    # 书和出版社是一对多的关系,并且书是查询多的一方,所以外键字段放在书表里
    publish = models.ForeignKey('Publish', on_delete=models.CASCADE)
    # 默认就是与出版社的主键字段关联

    # 图书和作者是多对多的关系
    authors = models.ManyToManyField('Author')
    # authors是一个虚拟字段,告诉orm,书表和作者是多对多的关系
    # 让orm帮你自动创建第三张关系表


class Publish(models.Model):
    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    # 作者和作者详情是一对一的关系
    # OneToOneField
    author_detail = models.OneToOneField('AuthorDetail', on_delete=models.CASCADE)


class AuthorDetail(models.Model):
    phone = models.BigIntegerField()
    addr = models.CharField(max_length=64)