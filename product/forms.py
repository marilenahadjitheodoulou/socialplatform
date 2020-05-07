from django import forms
from django.contrib.auth.models import User

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'state_type')#, 'image')
    
    def save(self, commit=True):
        user = super().save(commit=False)

        user.category = self.cleaned_data['category']
        user.title = self.cleaned_data['title']
        user.description = self.cleaned_data['description']        
        user.state_type = self.cleaned_data['state_type']
        #user.image = self.cleaned_data['image']


        if commit:
            user.save()
        return user