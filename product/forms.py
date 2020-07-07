from django import forms
from django.contrib.auth.models import User
from .models import Product, Subcategory, ProductInterest

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'subcategory', 'title', 'description', 'state_type', 'image', 'extra_image')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcategory'].queryset = Subcategory.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set.order_by('name')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.category = self.cleaned_data['category']
        user.subcategory = self.cleaned_data['subcategory']
        user.title = self.cleaned_data['title']
        user.description = self.cleaned_data['description']        
        user.state_type = self.cleaned_data['state_type']
        user.image = self.cleaned_data['image']
        user.extra_image = self.cleaned_data['extra_image']

        if commit:
            user.save()
        return user

class InterestForm(forms.ModelForm):
    class Meta:
        model = ProductInterest
        fields = ('product', 'title', 'status')
    
    def save(self, commit=True):
        user = super().save(commit=False)

        user.product = self.cleaned_data['product']
        user.title = self.cleaned_data['title']
        user.status = self.cleaned_data['status']

        if commit:
            user.save()
        return user