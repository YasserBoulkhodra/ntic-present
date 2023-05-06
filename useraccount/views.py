from django.shortcuts import render
from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,get_user_model
from django.http import HttpResponse
from django.contrib import messages
from .forms import *

from rest_framework import generics, mixins, response, status, permissions
from . import serializers

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_student:
                login(request, user)
                return redirect('student')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('teacher')
            elif user is not None and user.is_headdep:
                login(request, user)
                return redirect('headdep')
            
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})





def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
       
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})



def student(request):
    return render(request,'student.html')
    
def teacher(request):
    return render(request,'teacher.html')
    
def headdep(request):
    return render(request,'headdep.html')
 
def login_view(request):
    return render(request,'login.html')




def test():
    return User.objects.all()

class UserAPIView(generics.ListCreateAPIView, mixins.UpdateModelMixin):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

    
    
class UserRetrieveAPIView(generics.RetrieveAPIView, mixins.DestroyModelMixin):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.filter()
    permission_classes = [permissions.IsAuthenticated]

    