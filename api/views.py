from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

def register_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'api/register.html', {'form': form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('spa')
            

        else:
            return render(request, 'api/register.html', {'form': form})


def login_view(request: HttpRequest) -> HttpResponse:
        if request.method == 'GET':
            form = LoginForm()
            return render(request, 'api/login.html', {'form': form})

        elif request.method == 'POST':
            form = LoginForm(request.POST)
            
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request,username=username,password=password)
                if user:
                    login(request, user)
                    messages.success(request,f'Hi {username.title()}, welcome back!')
                    return redirect('spa')
            
            # form is not valid or user is not authenticated
            messages.error(request,f'Invalid username or password')
            return render(request,'api/login.html',{'form': form})

def logout_view(request: HttpRequest) -> HttpResponse:
    return render(request,'api/login.html',{'form': form})

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            # Logic for successful authentication
            # You need to add logic here, such as returning a success response
            return Response({"message": "User authenticated"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
