
from django.urls import  path

from . import views
from .views import PostListView,ArticleDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns=[
#APIS ENDPOINT STARTS
path('posts/',views.PostsView.as_view(),name="get-create-posts"),
path('edit-posts/<int:id>/',views.EditPostsView.as_view(),name="edit-delete-posts"),

#APIS ENDPOINT END


#path('',views.home, name="blog-home"),
#path('about/',views.about, name="blog-about"),
path('',PostListView.as_view(),name="blog-home"),
path('search/', views.search,name='search'),
path('post/create/',PostCreateView.as_view(),name="blog-create"),
path('post/<int:pk>/', ArticleDetailView.as_view(),name="blog-article"),
path('post/<int:pk>/update/', PostUpdateView.as_view(),name="blog-update"),
path('post/<int:pk>/delete/', PostDeleteView.as_view(),name="blog-delete"),

]