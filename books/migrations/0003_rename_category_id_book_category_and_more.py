# Generated by Django 4.1.7 on 2023-04-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author_id',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='books.author'),
        ),
    ]