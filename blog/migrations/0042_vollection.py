# Generated by Django 2.2.1 on 2019-09-29 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_auto_20190929_0458'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolLection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.IntegerField(choices=[(0, 'Взаимодействие с людьми с органиченными возможостями'), (1, 'Взаимодействие с детьми'), (2, 'Ораторские качества'), (3, 'Что нибудь еще')], default=0)),
                ('strength', models.IntegerField(default=1)),
                ('perception', models.IntegerField(default=1)),
                ('endurance', models.IntegerField(default=1)),
                ('charisma', models.IntegerField(default=1)),
                ('agility', models.IntegerField(default=1)),
                ('luck', models.IntegerField(default=1)),
                ('description', models.TextField(blank=True, default='', max_length=500)),
            ],
        ),
    ]