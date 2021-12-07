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
    user = CurrentUserField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    like = models.ManyToManyField(get_user_model(), through='Like', related_name='like', blank=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
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
    def like_count(self) -> int:
        return self.post_like.count()


    def remove_like(self, user):
        self.post_like.get(user=user).delete()

    def add_like(self, user):
        self.post_like.create(user=user, post=self)


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


class Like(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), related_name='user_like', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='post_like', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} liked {self.post}'