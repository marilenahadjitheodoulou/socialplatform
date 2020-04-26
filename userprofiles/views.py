from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from userprofiles.models import UserProfile
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
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            login(request, user)

            return redirect('login')
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'registration/register.html', context)

    
class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    updateform = UserRegisterForm
    updateprofile_form = UserProfileForm
    template_name = 'registration/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        updateform = UserRegisterForm(post_data, instance=request.user)
        updateprofile_form = UserProfileForm(post_data, file_data, instance=request.user)

        if updateform.is_valid() and updateprofile_form.is_valid():
            updateform.save()
            updateprofile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return redirect('profile')

        context = self.get_context_data(
                                        updateform=updateform,
                                        updateprofile_form=updateprofile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


@login_required
def profile(request):
    #print(request.user)
    #userprofile = UserProfile.objects.get(user_id=request.user.id)
    #print(userprofile.user_type)
    return render(request, 'registration/profile.html')

        
