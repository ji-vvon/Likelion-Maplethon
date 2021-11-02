# Generated by Django 3.2.9 on 2021-11-02 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20211103_0036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='majorbook',
            old_name='img',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='majorbook',
            name='category',
            field=models.TextField(choices=[('IT', 'IT'), ('인문', '인문'), ('사회', '사회'), ('과학', '과학'), ('예술', '예술')]),
        ),
    ]