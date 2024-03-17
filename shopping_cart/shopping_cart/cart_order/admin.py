from django.contrib import admin

from shopping_cart.cart_order.models import OrderItem, ShoppingCart


# Register your models here.
@admin.register(OrderItem)
class ModelNameAdmin(admin.ModelAdmin):
    pass


@admin.register(ShoppingCart)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'ordered')
