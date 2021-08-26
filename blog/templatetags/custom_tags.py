from django import template
from blog.models import Like

register = template.Library()


@register.simple_tag
def liked(user, post):
    return 'favrotie' if Like.objects.filter(user=user, post=post) else 'favorite_border'