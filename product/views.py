from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .forms import ProductForm, InterestForm
from .models import *
from django.core.files.storage import FileSystemStorage
from .filters import OrderFilter
from userprofiles.models import User

def upload(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.save()

            messages.success(request, f'Your product has been created!')

            return redirect('product:myproducts')
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, 'registration/upload.html', context)

class UploadView(TemplateView):
    template_name = 'registration/myproducts.html'

    def get(self, request):
        products = Product.objects.filter(user=request.user)
        total_myproduct = products.count()
        context = {'products': products, 'total_myproduct':total_myproduct}
        return render(request, self.template_name, context)

class ProductView(TemplateView):
    template_name = 'registration/products.html'

    def get(self, request):
        allproducts = Product.objects.filter()
        
        tot = Product.objects.all()
        total_product = allproducts.count()

        myFilter = OrderFilter(request.GET, queryset=tot)
        tot = myFilter.qs
        context = {'allproducts': allproducts, 'tot': tot, 'total_product':total_product, 'myFilter': myFilter}
        return render(request, self.template_name, context )

def load_subcategories(request):    
    category_id = request.GET.get('category')
    subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'registration/load_subcategories.html', {'subcategories': subcategories})

def createInterest(request):
    if request.method == 'POST':
        form = InterestForm(request.POST)

        if form.is_valid():
            createInterest = form.save(commit=False)
            createInterest.user = request.user
            createInterest.save()
            
            return redirect('product:wishlist')
    else:
        form = InterestForm()

    context = {'form': form}
    return render(request, 'registration/interest.html', context)

def wishlist(request):
    interests = ProductInterest.objects.all()
    context = {'interests':interests}
    return render(request, 'registration/wishlist.html', context)

def deleteInterest(request, pk):
    interest = ProductInterest.objects.get(id=pk)
    if request.method == "POST":
        interest.delete()
        return redirect('product:products')

    context = {'item': interest}
    return render(request, 'registration/delete.html', context)
