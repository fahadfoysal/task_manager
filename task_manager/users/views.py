from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/users_register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,
                                password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'You have logged in.')
                return redirect('task_list')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form':form})


def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html')