# Generated by Django 2.2.1 on 2019-09-27 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_userprofile_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='slug',
            new_name='user_url',
        ),
    ]
