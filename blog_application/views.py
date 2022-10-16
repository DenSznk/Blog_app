from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, DeleteView

from blog_application.forms import PostForm
from blog_application.models import Post
from blog_application.services import get_post_list, get_detail_post


def posts_list_view(request):
    """Rendering a list of all posts """

    lst = Paginator(get_post_list(request), 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    return render(request, 'posts_list.html', {'page_obj': page_obj})


def post_detail_view(request, pk=None):
    """Rendering a post """

    if pk:
        post = get_detail_post(request, pk)
        return render(request, 'post_detail.html', {'post': post})


class PostCreateView(CreateView):
    """ View for creating new Post """
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('posts_list')

    def form_valid(self,  form):
        post = form.save(commit=False)
        post.post_author = User.objects.get(pk=self.request.user.id)
        post.save()
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    """ Post updating view """
    model = Post
    form_class = PostForm
    template_name = 'post_update.html'
    success_url = reverse_lazy('posts_list')
    success_message = f"City was update"


class PostDeleteView(DeleteView):
    """ Post updating view """
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')

