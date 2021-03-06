from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def store(request, Category_slug=None):
    categories = None
    products = None

    if Category_slug != None:
        categories = get_object_or_404(Category, slug=Category_slug)
        products = Product.objects.all().filter(Category=categories, is_available=True)
        product_count = products.count()
    else:
       products = Product.objects.all().filter(is_available=True)
       product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)
