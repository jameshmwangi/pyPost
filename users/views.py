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
from rest_framework.parsers import JSONParser
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
    parser_classes = [JSONParser]

    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        user = User.objects.get(username=username)
        refresh = RefreshToken.for_user(user)
        data = {'refresh': str(refresh),'access': str(refresh.access_token)}
        return Response(data,status=status.HTTP_200_OK)





    