from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status, generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import *


# Create your views here.
def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST )
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Dear {username} Your AccountHas Been Successfully Created, Kindly SIGN IN ')
            return redirect('login')

    else:        
            form=UserRegisterForm()

    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')


def profile_update(request):
    if request.method=="POST":
        u_form= UserUpdateForm(request.POST,instance=request.user)
        p_form= ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Profile Successfully Updated')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)


    context={
        "u_form":u_form,
        "p_form":p_form
    }
    return render(request,'users/profile_update.html',context)

class ApiAuthentication(generics.CreateAPIView):
    serializer_class=LoginSerializer

    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=User.objects.filter(username=username)
        if not user:
            return Response({'Validation_error ':'Invalid username or passwords'},status=status.HTTP_403_FORBIDDEN)
        if user.first().check_password(password):
            try:
                token = Token.objects.create(user=user.first())
            except:
                 token = Token.objects.get(user=user.first())
            return Response({'token':token.key},status=status.HTTP_200_OK)
        else:
            return Response({'Validation_error ':'Invalid username or password'},status=status.HTTP_403_FORBIDDEN)






    