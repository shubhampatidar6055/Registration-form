# Generated by Django 5.0.4 on 2024-04-25 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_user_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
    ]
