from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from dal import autocomplete

from blog.models import Post, Category
from blog.forms import PostForm, LikePostForm


class CustomPermissionRequiredMixin(PermissionRequiredMixin):
    permission_required = 'post.edit'

    def has_permission(self):
        return super().has_permission() and self.request.user == self.get_object().user


class CategoryAutoCompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Category.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs


class PostListView(ListView):
    model = Post
    template_name_suffix = '_list'
    context_object_name = 'posts'
    extra_context = {'title': 'Post List'}


class PostDetailView(DetailView):
    model = Post
    template_name_suffix = '_detail'
    context_object_name = 'post'

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return redirect(reverse_lazy('blog:home'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'
    model = Post
    template_name_suffix = '_form'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('blog:post-detail', kwargs={'pk': self.object.pk, 'slug': self.object.slug})


class PostUpdateView(CustomPermissionRequiredMixin, UpdateView):
    model = Post
    template_name_suffix = '_form'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('blog:post-detail', kwargs={'pk': self.object.pk, 'slug': self.object.slug})


class PostDeleteView(CustomPermissionRequiredMixin, DeleteView):
    model = Post
    template_name_suffix = '_delete'

    def get_success_url(self, *args, **kwargs):
        return reverse('blog:post-list', args=args, kwargs=kwargs)


class LikePostView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    template_name = 'blog/components/buttons/like_button.html'
    model = Post
    form_class = LikePostForm

    def get_success_url(self):
        return reverse_lazy('blog:post-like', kwargs={'pk': self.object.pk, 'slug': self.object.slug})