from blog_application.models import Post


def get_post_list(request):
    """Getting a list of all posts """

    posts_list = Post.objects.prefetch_related('post_author', 'post_category').order_by('-post_date_added')
    return posts_list


def get_detail_post(request, pk):
    """Getting a single post"""
    post_detail = Post.objects.get(id=pk)
    return post_detail



