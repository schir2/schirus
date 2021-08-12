from dal import autocomplete
from django import forms
from blog.models import Post
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
        if post in user.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
        return post

    def clean(self):
        self.user = User.objects.get(pk=self.initial.get('user'))
        cleaned_data = super().clean()
        return cleaned_data