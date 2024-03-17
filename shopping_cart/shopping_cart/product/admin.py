from django.contrib import admin

from shopping_cart.product.models import Category, Products


# Register your models here.
@admin.register(Category)
class ModelNameAdmin(admin.ModelAdmin):
    pass


@admin.register(Products)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'price')
