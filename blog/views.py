from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from dal import autocomplete

from blog.models import Post, Category
from blog.forms import PostForm


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


class PostDetailView(DetailView):
    model = Post
    template_name_suffix = '_detail'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name_suffix = '_form'
    form_class = PostForm


class PostUpdateView(UpdateView):
    model = Post
    template_name_suffix = '_form'
    form_class = PostForm


class PostDeleteView(DeleteView):
    model = Post
    template_name_suffix = '_delete'
