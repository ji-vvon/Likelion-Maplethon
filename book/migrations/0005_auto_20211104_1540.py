# Generated by Django 3.1.3 on 2021-11-04 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20211104_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowedbook',
            old_name='book_pk',
            new_name='borrow_book',
        ),
    ]
