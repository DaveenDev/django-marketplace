from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('product/<slug:slug>', views.product_detail, name='product-detail')
]
