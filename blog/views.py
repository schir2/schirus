from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView
from django.urls import reverse
from django.http import HttpResponse, JsonResponse

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

    def get_success_url(self, *args, **kwargs):
        return reverse('blog:post-list', args=args, kwargs=kwargs)


class PostUpdateView(UpdateView):
    model = Post
    template_name_suffix = '_form'
    form_class = PostForm

    def get_success_url(self, *args, **kwargs):
        return reverse('blog:post-list', args=args, kwargs=kwargs)


class PostDeleteView(DeleteView):
    model = Post
    template_name_suffix = '_delete'

    def get_success_url(self, *args, **kwargs):
        return reverse('blog:post-list', args=args, kwargs=kwargs)


def like_post_view(request):
    # TODO Finish Ajax JS Method
    if request.method == 'POST':
        user = request.user
        post_id = request.POST.get('post_id')
        post = Post.objects.get(pk=post_id)
        context = {
            'post_id': post_id,
        }
        if user.username in post.liked_by:
            post.likes.remove(user)
            context['like'] = False
        else:
            post.likes.add(user)
            context['like'] = True
        return JsonResponse(context)
