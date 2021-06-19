from django.shortcuts import render
from django.shortcuts import reverse, redirect


def redirect_to_blog_view(request):
    return redirect(reverse('blog:post-list'))