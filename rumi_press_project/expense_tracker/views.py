from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.

@login_required(login_url='auth_choice')
def home(request):
    return render(request, 'home.html', {'user': request.user})


def auth_choice(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'auth_choice.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        messages.success(request, 'Logged in successfully.')
        return redirect('home')
    
    if not form.is_valid():
        messages.error(request, "Invalid username or password.") 

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Registration complete. You are now logged in.')
        return redirect('home')

    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('auth_choice')
