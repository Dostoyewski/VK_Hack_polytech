# Generated by Django 2.2.1 on 2019-09-29 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0039_userprofile_forschung_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='karma_reward',
            field=models.FloatField(default=0),
        ),
    ]
