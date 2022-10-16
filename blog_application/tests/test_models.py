from django.contrib.auth.models import User
from django.test import TestCase
from blog_application.models import Post, Category, PostCategory


class TestModels(TestCase):
    def setUp(self):
        self.post_author = User.objects.create(
            id=1,
            username='User1',
        )
        self.post1 = Post.objects.create(
            post_header='Test Header',
            post_content='Test Content',
            post_author=self.post_author,
            post_tag='NE',
        )

    def test_post_author(self):
        self.assertEquals(self.post1.post_author, self.post_author)
