from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import (
    LogoutView as BaseLogoutView
)

class LogInView(LoginRequiredMixin, TemplateView):
    template_name = 'login.html'

class LogOutView(LoginRequiredMixin, BaseLogoutView):
    template_name = 'logout.html'