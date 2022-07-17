from django.urls import resolve,reverse
from urllib import response
from django.test import TestCase
from blog.views import search,PostListView,ArticleDetailView,PostCreateView,PostUpdateView,PostDeleteView

class UrlsTest(TestCase):
    def test_testhomepage(self):
        response=self.client.get('/')
        self.assertEquals(response.status_code,200)  

    def test_search_url_resolved(self):
        url=reverse('search')
        self.assertEquals(resolve(url).func, search )

    def test_post_url_resolved(self):
        url=reverse('blog-create')
        self.assertEquals(resolve(url).func.view_class, PostCreateView )
