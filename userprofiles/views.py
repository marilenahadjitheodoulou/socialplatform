from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import (
    LogoutView as BaseLogoutView
)
class LogInView(LoginRequiredMixin, TemplateView):
    template_name = 'login.html'

class LogOutView(LoginRequiredMixin, BaseLogoutView):
    template_name = 'logout.html'

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })
    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            messages.success(request, f'Your account has been created! You are now able to log in')
            login(request, user)

            return redirect('login')
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()

    context = {'form' : form, 'profile_form' : profile_form}
    return render(request, 'registration/register.html', context)

@login_required
def profile(request):
    return render(request, 'registration/profile.html')