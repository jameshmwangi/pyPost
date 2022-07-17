from http import client
from urllib import response
from django.test import TestCase , Client
from django.urls import reverse
from blog.views import PostListView,ArticleDetailView,PostCreateView,PostUpdateView,PostDeleteView
import json


class ViewsTest(TestCase):
    def test_post_list(self):
        client=Client()
        response= client.get(reverse('',args=['home']))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/home.html')
