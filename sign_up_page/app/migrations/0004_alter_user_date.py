# Generated by Django 5.0.4 on 2024-04-25 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateField(null=True),
        ),
    ]