# Generated by Django 3.2.9 on 2021-11-04 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='MajorBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=30)),
                ('pub_date', models.DateField(blank=True, null=True)),
                ('info_text', models.TextField(max_length=200)),
                ('img', models.ImageField(blank=True, null=True, upload_to='book/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('대여 가능', '대여 가능'), ('대여중', '대여중')], default='대여가능', max_length=10)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.category')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
