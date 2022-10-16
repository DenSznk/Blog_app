from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
import json
from blog_application.models import Post, Category


class TestViews(TestCase):

    def setUp(self):
        self.post_author = User.objects.create(
            id=1,
            username='User1',
        )
        self.client = Client()
        self.posts_url = reverse('posts_list')
        self.post_detail_url = reverse('posts_detail', args=[1])
        self.post1 = Post.objects.create(
            post_header='Test Header',
            post_content='Test Content',
            post_author=self.post_author,
            post_tag='NE',
        )

    def test_post_list_get_status_code(self):
        response = self.client.get(self.posts_url)
        self.assertEquals(response.status_code, 200)

    def test_post_list_get_template(self):
        response = self.client.get(self.posts_url)
        self.assertTemplateUsed(response, 'posts_list.html')

    def test_post_detail_get_status_code(self):
        response = self.client.get(self.post_detail_url)
        self.assertEquals(response.status_code, 200)

    def test_post_detail_get_template(self):
        response = self.client.get(self.post_detail_url)
        self.assertTemplateUsed(response, 'post_detail.html')
