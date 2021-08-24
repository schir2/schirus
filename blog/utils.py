from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

user = User.objects.all()[0]

for i in range(100):
    Post.objects.create(
        title=f'Test Post Title {i}',
        content=f'Test Content {i}',
        subtitle=f'Test Subtitle {i}',
        user=user,
    )