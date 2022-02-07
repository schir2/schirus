from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.name
