from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from .forms import LoginForms, RegisterUserForms, PasswordResetForms
from users.models import User


def home(request):
    form = LoginForms()
    if request.user.is_authenticated:
        return redirect('booking')
    return render(request, 'registration/login.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(
                request=request, 
                username=clean_data['username'],
                password=clean_data['password']
            )
            if user is not None:
                if user.is_active:
                    login(request=request, user=user)
                    return redirect('booking')
                else:
                    return redirect('login')

    return redirect('home')


def logout_user(request):
    logout(request=request)
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForms(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            if user is not None:
                return redirect('login')
    form = RegisterUserForms()
    return render(request, 'registration/register_user.html', {'form': form})


def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForms(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.get(email=data['email'])
            user.password = make_password(data['new_password'])
            user.save()
            return redirect('home')
        else:
            return render(request, 'registration/password_reset.html', {'form': form})
    form = PasswordResetForms()
    return render(request, 'registration/password_reset.html', {'form': form})
