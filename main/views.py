from django.shortcuts import render
from .models import Product
from django.conf import settings

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'main/home.html', {
        'products': products
    })

def product_detail(request,slug):
    product = Product.objects.get(slug=slug)
    stripe_public_key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'main/product_detail.html', {
        'product': product,
        'stripe_public_key': stripe_public_key
    })
