from os import path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


def get_media_upload_path(instance, filename):
    return path.join(
        settings.MEDIA_ROOT,
        'users',
        str(instance.author.id),
        instance.__class__.__name__,
        filename,
    )


class Article(models.Model):
    slug = models.SlugField(default="", editable=False, max_length=60)
    title = models.CharField(max_length=60)
    content = models.TextField()
    user = models.ForeignKey(get_user_model(), related_name='user', on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', related_name='articles', blank=True)
    likes = models.ManyToManyField(get_user_model(), through='Like', related_name='articles', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)


class Category(models.Model):
    slug = models.SlugField(default="", editable=False, max_length=60)
    name = models.CharField(max_length=60, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            self.name = self.name.lower()
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Like(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} liked {self.article}'
