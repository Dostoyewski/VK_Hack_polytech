# Generated by Django 2.2.1 on 2019-09-28 11:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_auto_20190928_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reg_ending_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 28, 14, 58, 15, 962433)),
            preserve_default=False,
        ),
    ]
