# Generated by Django 2.2.1 on 2019-09-13 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='beginning_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='ending_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='idd',
        ),
    ]