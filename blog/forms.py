from dal import autocomplete
from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {'category': autocomplete.ModelSelect2(url='blog:category-autocomplete')}