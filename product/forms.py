from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product
from userprofiles.forms import UserRegisterForm
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'state_type')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.category = self.cleaned_data['category']
        user.state_type = self.cleaned_data['state_type']

        if commit:
            user.save()
        return user
