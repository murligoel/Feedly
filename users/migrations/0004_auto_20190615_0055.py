# Generated by Django 2.1.5 on 2019-06-15 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190615_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='avatar',
            field=models.ImageField(default='//static/profile.png', upload_to='profile_pic'),
        ),
    ]