# Generated by Django 5.0.3 on 2024-03-27 07:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('places', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place'),
        ),
        migrations.AddField(
            model_name='placeowner',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.owner'),
        ),
        migrations.AddField(
            model_name='placeowner',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.place'),
        ),
    ]
