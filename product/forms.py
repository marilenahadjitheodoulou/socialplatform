from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('state_type', 'categories_type', 'subcategories_type')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.state_type = self.cleaned_data['state_type']
        user.categories_type = self.cleaned_data['categories_type']
        user.subcategories_type = self.cleaned_data['subcategories_type']

        if commit:
            user.save()
        return user
