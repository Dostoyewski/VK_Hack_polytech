# Generated by Django 2.2.1 on 2019-09-18 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190916_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='karma',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default='Не заполнено', max_length=500),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(default='Не указан', max_length=30),
        ),
    ]
