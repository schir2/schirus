from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from allauth.account.signals import user_logged_in
from allauth.socialaccount.signals import pre_social_login
from django.dispatch import receiver
from django.core import files
from sorl.thumbnail import get_thumbnail

from users.ustils import download_image


@receiver(pre_social_login)
def get_profile_picture(sender, **kwargs):
    print(kwargs)


class User(AbstractUser):

    def __str__(self):
        return f'{self.username}'

    @property
    def name(self):
        return ' '.join(
            name for name in [self.first_name, self.last_name] if name
        ) or self.username


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    social_avatar = models.ImageField(blank=True, null=True)
    profile_avatar = models.ImageField(blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.name


@receiver(user_logged_in)
def get_avatar(sociallogin, user, **kwargs):
    if sociallogin.account.provider == 'google':
        url = sociallogin.account.extra_data['picture']
        if url:
            fp = download_image(url)
            if fp:
                file_name = 'social_avatar.jpeg'
                print(fp)
                fp = get_thumbnail(
                    fp,
                    '64x64',
                    quality=99, format='JPEG'
                )
                user.profile.profile_avatar = fp
                user.profile.save()