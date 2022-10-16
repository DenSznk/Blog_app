from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog_application.views import posts_list_view, post_detail_view, PostCreateView


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('posts_list')
        self.assertEquals(resolve(url).func, posts_list_view)

    def test_create_url_is_resolved(self):
        url = reverse('posts_create')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_post_detail_url_is_resolved(self):
        url = reverse('posts_detail', args=[1])
        self.assertEquals(resolve(url).func, post_detail_view)
