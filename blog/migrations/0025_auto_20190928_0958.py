# Generated by Django 2.2.1 on 2019-09-28 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_remove_userprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='karma',
            field=models.FloatField(default=0),
        ),
    ]
