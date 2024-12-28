from django.shortcuts import render, redirect
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import AddProductForm

@login_required
def product_details(request, pk):
    detail = Product.objects.get(pk=pk)
    context = {
        'detail' : detail
    }
    return render(request, "details.html", context)


@login_required
def all_products(request):
    products = Product.objects.all()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(products, 10)
    page_obj = paginator.get_page(page_number)
    page_range = paginator.get_elided_page_range(number=page_obj.number, on_each_side=3, on_ends=2)
    context = {
        "products" : page_obj,
        "page_range" : page_range
    }
    return render(request, "admin.html", context)

def add_products(request):
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("all_products")
    else:
        form = AddProductForm()

    context = {
        "form" : form
    }
    return render(request, "add.html", context)

def update_product(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("all_products")
    else:    
        form = AddProductForm(instance=product)

    context = {
        "product" : product
    }
    return render(request, "update.html", context)
    
def delete_product(request, pk):
    form = Product.objects.get(pk=pk)
    form.delete()
    return redirect("all_products")