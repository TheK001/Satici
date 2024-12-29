from django.shortcuts import render
from product.models import Product
from django.core.paginator import Paginator

def home(request):
    search = request.GET.get('q')
    if search is not None and search != "":
        products = Product.objects.filter(name__icontains=search)
    else:
        products = Product.objects.all()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(products, 12)
    page_obj = paginator.get_page(page_number)
    page_range = paginator.get_elided_page_range(number=page_obj.number, on_each_side=3, on_ends=2)
    context = {
        "search" : search,
        "products" : page_obj,
        "page_range" : page_range
    }
    return render(request,"index.html", context)

