from django.db import models
from abc import ABCMeta, abstractmethod
from django_currentuser.db.models import CurrentUserField
from os import path
from django.conf import settings


def get_media_upload_path(instance, filename):
    return path.join(
        settings.MEDIA_ROOT,
        'users',
        str(instance.author.id),
        instance.__class__.__name__,
        filename,
    )


class AbstractPost(models.Model):

    slug = models.SlugField()
    title = models.CharField(max_length=60)
    author = CurrentUserField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    @abstractmethod
    def snippet(self):
        pass

    @abstractmethod
    def graphic(self):
        pass

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Article(AbstractPost):
    image = models.ImageField(upload_to=get_media_upload_path)

    def snippet(self):
        return self.title

    def graphic(self):
        return self.image