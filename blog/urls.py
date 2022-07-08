from unicodedata import name
from django.urls import  path

from . import views
from .views import PostListView,ArticleDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns=[
#path('',views.home, name="blog-home"),
#path('about/',views.about, name="blog-about"),
path('',PostListView.as_view(),name="blog-home"),
path('post/create',PostCreateView.as_view(),name="blog-create"),
path('post/<int:pk>/', ArticleDetailView.as_view(),name="blog-article"),
path('post/<int:pk>/update', PostUpdateView.as_view(),name="blog-update"),
path('post/<int:pk>/delete', PostDeleteView.as_view(),name="blog-delete"),

]