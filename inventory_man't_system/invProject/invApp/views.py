from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.

# Home View
def home_view(request):
  return render(request, 'invApp/home.html')

# CRUD = Create, Read, Update, Delete
# Create View
def create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'invApp/create.html', {'form': form})


# Read View
def product_list(request):
    products = Product.objects.all()
    return render(request, 'invApp/product_list.html', {'products': products})
# Update View
def update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'invApp/update.html', {'form': form})
# Delete View
def delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'invApp/product_confirm_delete.html', {'product': product})
    


