from django.core.paginator import Paginator
from django.shortcuts import render

from blog_application.models import Post


def posts_list_view(request):
    posts_list = Post.objects.prefetch_related('post_author', 'post_category').order_by('-post_date_added')
    lst = Paginator(posts_list, 5)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'posts_list.html', context)


def post_detail_view(request, pk=None):
    if pk:
        post = Post.objects.filter(id=pk).first()
        context = {'post': post}
        return render(request, 'post_detail.html', context)
