# Generated by Django 2.2.12 on 2022-09-11 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20220911_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='info',
            field=models.CharField(default='jjy', max_length=32),
        ),
    ]