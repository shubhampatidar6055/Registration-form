# Generated by Django 5.0.4 on 2024-04-25 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='City', max_length=150),
        ),
    ]
