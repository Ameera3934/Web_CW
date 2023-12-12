from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

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

