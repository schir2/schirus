# Generated by Django 4.0.2 on 2022-02-15 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_remove_like_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]