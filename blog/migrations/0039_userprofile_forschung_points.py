# Generated by Django 2.2.1 on 2019-09-29 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_auto_20190928_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='forschung_points',
            field=models.FloatField(default=0),
        ),
    ]
