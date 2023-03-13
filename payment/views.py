from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.urls import reverse
from main.models import Product
import stripe, json

# Create your views here.

@csrf_exempt
def create_checkout_session(request,id):
    request_data = json.load(request.body)
    product = Product.objects.get(pk=id)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        customer_email = request_data['email'],
        payment_method_types = ['card'],
        line_items=[
            {
              'price_data': {
                  'currency': 'usd',
                  'product_data':{
                      'name': product.name
                  },
                  'unit_amount': float(product.price),
              },
              'quantity':1
            }
        ],
        mode='payment',
        success_url = request.build_absolute_uri(reverse('success')) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('failed')),
    )
