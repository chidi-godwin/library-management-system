# Generated by Django 4.1.7 on 2023-04-11 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
