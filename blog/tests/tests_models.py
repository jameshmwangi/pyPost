from turtle import title
from django.test import TestCase
from blog.models import Post

"""class ModelTesting(TestCase):
    def setUp(self):
        self.blog =Post.objects.create(title='job1', content='now hiring', authour_id=2 )
    def test_post_model(self):
        a=self.blog
        self.assertTrue(isinstance(a,Post))
        self.assertEqual(str(a), 'job1')
        
"""