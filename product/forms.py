from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('state_type', 'category', 'subcategory')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.state_type = self.cleaned_data['state_type']
        user.category = self.cleaned_data['category']
        user.subcategory = self.cleaned_data['subcategory']

        if commit:
            user.save()
        return user
