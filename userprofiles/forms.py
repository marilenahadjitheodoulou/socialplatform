from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import UserProfile, Ngodetails


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'email', 
        ]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('location', 'number', 'user_type')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.location = self.cleaned_data['location']
        user.number = self.cleaned_data['number']
        user.user_type = self.cleaned_data['user_type']

        if commit:
            user.save()
        return user

class EditProForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'location', 
            'number', 
        ]

class NgodetailsForm(forms.ModelForm):
    class Meta: 
        model = Ngodetails
        fields = ('pdf',)

    def save(self, commit=True):
        user = super().save(commit=False)

        user.pdf = self.cleaned_data['pdf']

        if commit:
            user.save()
        return user