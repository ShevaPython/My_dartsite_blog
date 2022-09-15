from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL категории', )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='Тег')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименования')
    content = models.TextField(blank=True, verbose_name='Контент')
    author = models.CharField(max_length=100, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_publish = models.BooleanField(default=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', related_name='posts')
    view = models.IntegerField(default=0, verbose_name='Количество просмотров')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL тега')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
