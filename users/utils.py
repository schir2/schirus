from io import BytesIO
from PIL import Image
from django.core import files
from django.contrib.auth import get_user_model

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


def resize_to_avatar(infile: BytesIO) -> BytesIO:
    outfile = BytesIO()
    image = Image.open(infile, 'r')
    #image = image.resize((64,64), Image.ANTIALIAS)
    image.save(outfile, format='JPEG', quality=100)
    outfile.seek(0)
    return outfile


if __name__ == '__main__':
    fp = download_image('https://pocket-syndicated-images.s3.amazonaws.com/5ddedbe927fc7.jpg')
    resized = resize_to_avatar(fp)
    f = files.File(resized)
    Users = get_user_model()
    p = Users.objects.all()[0].profile
    p.profile_avatar.save('test.jpg', resized)
