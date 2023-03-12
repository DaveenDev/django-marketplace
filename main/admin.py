from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

    class Meta:
        verbose_name_plural = "Products"

admin.site.register(Product, ProductAdmin)