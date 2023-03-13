from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    prepopulated_fields = { 'slug': ('name',)}
    class Meta:
        verbose_name_plural = "Products"

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)