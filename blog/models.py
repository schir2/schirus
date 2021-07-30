from django.db import models
from django_currentuser.db.models import CurrentUserField
from os import path
from django.conf import settings
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from django.utils.text import slugify


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
    subtitle = models.CharField(max_length=255)
    author = CurrentUserField(editable=False, related_name='author')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    likes = models.ManyToManyField(get_user_model(), related_name='likes', blank=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('title', 'author',)
        ordering = ('-created_on',)

    def __str__(self):
        return self.title

    def convert_content_to_image(self):
        # TODO Implement this method
        return self.content

    @property
    def graphic(self):
        # TODO Implement this method
        return self.convert_content_to_image()

    @property
    def snippet(self):
        return self.subtitle

    @property
    def likes_count(self) -> int:
        return self.likes.count()

    @property
    def liked_by(self) -> set:
        return set(like['username'] for like in self.likes.all().values())

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
