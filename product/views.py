from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ProductForm


def upload(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, f'Your product has been created!')

            return redirect('profile')
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, 'registration/upload.html', context)
