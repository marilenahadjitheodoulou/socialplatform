from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .forms import ProductForm
from .models import Product, Subcategory, ProductCategory
from django.core.files.storage import FileSystemStorage


def upload(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.save()

            messages.success(request, f'Your product has been created!')

            return redirect('myproducts')
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, 'registration/upload.html', context)

class UploadView(TemplateView):
    template_name = 'registration/myproducts.html'

    def get(self, request):
        products = Product.objects.filter(user=request.user)

        return render(request, self.template_name, {'products': products})

def load_subcategories(request):    
    category_id = request.GET.get('category')
    subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'registration/load_subcategories.html', {'subcategories': subcategories})