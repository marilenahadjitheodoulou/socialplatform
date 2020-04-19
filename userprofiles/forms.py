from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


USER_TYPE_CHOICES = (
    ('CIVILIAN', 'Civilian'),
    ('NGO', 'N.G.O.')
)

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES)
    

    class Meta:
        model = User
        fields = ['user_type', 'username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.user_type = self.cleaned_data['user_type']

        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('location', 'number')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.location = self.cleaned_data['location']
        user.number = self.cleaned_data['number']

        if commit:
            user.save()
        return user
        
