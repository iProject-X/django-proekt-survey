from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Iltimos tizimga kiring"

    context = {"username": username}
    return render(request, 'index.html', context)


@login_required
def profile(request):
    return render(request, 'profile.html')

def startapp(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfil(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user =authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        else:
            form = ExtendedUserCreationForm()
            profile_form = UserProfil()
        
        context = {'form': form, 'profile_form': profile_form}
        return render(request, 'home.html', context)