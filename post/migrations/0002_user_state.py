# Generated by Django 4.2.6 on 2023-10-05 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.BooleanField(default=True),
        ),
    ]
