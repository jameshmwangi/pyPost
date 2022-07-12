from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from requests import post, request

from .models import Post
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# def home(request):
# context={
# 'posts':Post.objects.all()
# }
#  return render(request,'blog/home.html', context)

# def about(request):
#   return render(request,'blog/about.html', {'title':'About Page'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ["-date_posted"]


class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name='blog/article.html'
    context_object_name = 'posts'

class PostCreateView(LoginRequiredMixin,CreateView):
    model= Post
    
    fields=['title','content']
    template_name='blog/create.html'

    def form_valid(self, form) :
        form.instance.authour=self.request.user
        return super().form_valid(form)

    

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model= Post
    fields=['title','content']
    template_name='blog/edit.html'

    def form_valid(self, form) :
        form.instance.authour=self.request.user
        return super().form_valid(form)

    def test_func(self) :
        post= self.get_object()
        if self.request.user==post.authour:
            return True
        return False

class PostDeleteView(UserPassesTestMixin,DeleteView):
    model=Post
    
    context_object_name = 'posts'
    success_url='/'

    def test_func(self) :
        post= self.get_object()
        if self.request.user==post.authour:
            return True
        return False

