from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return f'{self.username}'

    def get_name_or_username(self):
        return ' '.join(
            name for name in [self.first_name, self.last_name] if name
        ) or self.username
