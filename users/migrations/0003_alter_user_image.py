# Generated by Django 5.0.3 on 2024-03-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='media/profile_pics/awdwa.jpg', upload_to='profile_pics/'),
        ),
    ]
