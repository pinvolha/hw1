from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    title = models.CharField('title', max_length=20)
    describe = models.TextField('description', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    text = models.TextField()
    show = models.BooleanField('show', default=True)
    #count = models.IntegerField('count', default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'post'
        verbose_name_plural = 'news'

    def __unicode__(self):
        return str(self.published_date)

    def url(self):
        return '/news/%s' % str(self.published_date)

    def __str__(self):
        return self.title


class Message(models.Model):
    chat = models.ForeignKey(Post, verbose_name='Обсуждение', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT)
    message = models.TextField('Сообщение')
    pub_date = models.DateTimeField('Дата сообщения', default=timezone.now)
