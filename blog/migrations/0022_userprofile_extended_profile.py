# Generated by Django 2.2.1 on 2019-09-27 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20190927_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='extended_profile',
            field=models.BooleanField(default=False),
        ),
    ]