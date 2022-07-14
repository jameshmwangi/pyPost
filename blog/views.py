from email import message
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post 
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status, generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from .serializers import *


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

class PostsView(generics.ListAPIView,generics.CreateAPIView): 
    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self,request):
        user =request.user 
        print(user)
        queryset = Post.objects.all()
        post_serializer=PostSerializer(queryset,many=True)
        return Response(post_serializer.data,status=status.HTTP_200_OK)


    def post(self,request):
        serializer= CreatePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class EditPostsView(generics.UpdateAPIView,generics.DestroyAPIView):
    authentication_classes=[JWTTokenUserAuthentication]
    permission_classes=[IsAuthenticated]

    def update(self,request,id):
        object_instance= Post.objects.get(id=id)
        serializer=EditPostSerializer(object_instance,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self,request,id):
        object_instance= Post.objects.get(id=id)
        object_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)