from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'main/home.html', {
        'products': products
    })

def product_detail(request,slug):
    product = Product.objects.get(slug=slug)

    return render(request, 'main/product_detail.html', {
        'product': product,
    })
