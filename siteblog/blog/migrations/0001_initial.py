# Generated by Django 4.1.1 on 2022-09-12 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тег')),
                ('slug', models.SlugField(unique=True, verbose_name='URL тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Наименования')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_publish', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/m%/d%/', verbose_name='Фото')),
                ('view', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('slug', models.SlugField(unique=True, verbose_name='URL тега')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.category', verbose_name='Категория')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='blog.tag')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-created_at'],
            },
        ),
    ]
