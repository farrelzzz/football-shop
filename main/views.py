from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product

def show_main(request):
    products_list = Product.objects.all()

    context = {
        # 'npm' : '240123456',
        'name': 'Muhammad Farrel Rajendra',
        'class': 'PBP D',
        'products_list': products_list
    }

    return render(request, "main.html", context)

def create_products(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_products.html", context)

def show_products(request, id):
    products = get_object_or_404(Product, pk=id)
    products.increment_views()

    context = {
        'products': products
    }

    return render(request, "products_detail.html", context)