# Generated by Django 4.1.7 on 2023-04-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_alter_cart_user_alter_cartitem_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
