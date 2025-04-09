from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.views.generic.base import TemplateView
from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

# Create your views here.

# Home View
# def home_view(request):
#   return render(request, 'invApp/home.html')

class HomeView(TemplateView):
    template_name = 'invApp/home.html'

# CRUD = Create, Read, Update, Delete
# Create View
# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('product_list')
#     return render(request, 'invApp/product_form.html', {'form': form})


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

# Read View
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'invApp/product_list.html', {'products': products})

# Update View
# def product_update_view(request, product_id):
#     product = Product.objects.get(product_id=product_id)
#     form = ProductForm(request.POST or None, instance=product)
#     if form.is_valid():
#         form.save()
#         return redirect('product_list')
#     return render(request, 'invApp/product_form.html', {'form': form})

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'invApp/product_form.html'
    success_url = reverse_lazy('product_list')

# Delete View
# def product_delete_view(request, product_id):
#     product = Product.objects.get(product_id=product_id)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('product_list')
#     return render(request, 'invApp/product_confirm_delete.html', {'product': product})
    


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')