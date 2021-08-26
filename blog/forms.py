from dal import autocomplete
from django import forms
from blog.models import Post, Like
from django.contrib.auth import get_user_model

User = get_user_model()


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {'category': autocomplete.ModelSelect2(url='blog:category-autocomplete')}


class LikePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('user', )

    def save(self, commit=True):
        post = super().save(commit=False)
        user = self.cleaned_data['user']
        like = Like.objects.filter(user=user, post=post).all()
        if like:
            like[0].delete()
        else:
            Like.objects.create(user=user, post=post)
        return post

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['user'] = User.objects.get(pk=self.initial.get('user'))
        return cleaned_data