# Generated by Django 2.2.5 on 2019-09-26 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Acc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, default='Не заполнено', max_length=500)),
                ('location', models.CharField(default='Не указан', max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('vorname', models.CharField(blank=True, max_length=20)),
                ('nachname', models.CharField(blank=True, max_length=50)),
                ('urlVK', models.CharField(blank=True, max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
