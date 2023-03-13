from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.urls import reverse
from main.models import Product, OrderDetail
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
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

    order = OrderDetail(
      customer_email = request_data['email'],
      product = product,
      amount = float(product.price),
      stripe_payment_intent = checkout_session['payment_intent']
    )
    order.save()

    return JsonResponse({
        'sessionID': checkout_session
    })

def payment_success(request):
    session_id = request.GET['session_id']
    if session_id is None:
        return HttpResponseNotFound()
    
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.retrieve(session_id)
    current_order = get_object_or_404(OrderDetail,stripe_payment_intent=session.payment_intent)
    current_order.has_paid = True
    current_order.save(update_fields=['has_paid'])
    return render(request, 'payment/succes.html',{
        'order': current_order
    })

def payment_failed(request):
    pass