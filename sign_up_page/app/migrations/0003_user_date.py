# Generated by Django 5.0.4 on 2024-04-25 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]