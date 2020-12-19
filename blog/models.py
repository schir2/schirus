from django.db import models
from abc import ABCMeta, abstractmethod
from django_currentuser.db.models import CurrentUserField
from os import path
from django.conf import settings
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.urls import reverse


def get_media_upload_path(instance, filename):
    return path.join(
        settings.MEDIA_ROOT,
        'users',
        str(instance.author.id),
        instance.__class__.__name__,
        filename,
    )


class Post(models.Model):

    slug = models.SlugField(default="", editable=False, max_length=60)
    title = models.CharField(max_length=60)
    content = HTMLField()
    snippet = models.CharField(max_length=255)
    author = CurrentUserField(editable=False, related_name='author')
    category = models.ManyToManyField('Category')
    likes = models.ManyToManyField(get_user_model(), related_name='like')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def convert_content_to_image(self):
        return self.content

    @property
    def graphic(self):
        return self.convert_content_to_image()

    @property
    def likes_count(self):
        return self.likes.count()

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug,
        }
        return reverse(f'post-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)


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
