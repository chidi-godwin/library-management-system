# Generated by Django 4.1.7 on 2023-04-12 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cart',
        ),
    ]