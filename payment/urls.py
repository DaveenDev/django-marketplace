from django.urls import path
from . import views
urlpatterns = [
    path('success', views.payment_success, name='success'),
    path('failed', views.payment_failed, name="failed")
]
