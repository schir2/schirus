from io import BytesIO

import requests


def create_user_profiles():
    from users.models import User, Profile
    for user in User.objects.filter(profile=None):
        Profile.objects.create(user=user)


def download_image(url: str):
    response = requests.get(url)
    fp = BytesIO()
    fp.write(response.content)
    return fp