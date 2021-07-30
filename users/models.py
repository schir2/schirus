from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from django.core import files
from users.ustils import download_image, resize_to_avatar


class User(AbstractUser):

    def __str__(self):
        return f'{self.username}'

    @property
    def name(self) -> str:
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

    @property
    def avatar(self):
        return self.profile_avatar or self.social_avatar

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
                resized_image = files.File(resize_to_avatar(fp))
                user.profile.social_avatar.save(file_name, resized_image)