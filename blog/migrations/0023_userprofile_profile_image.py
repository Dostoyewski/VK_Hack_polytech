# Generated by Django 2.2.1 on 2019-09-28 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_userprofile_extended_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='image_folder/None/no-img.jpg', upload_to='image_folder/'),
        ),
    ]