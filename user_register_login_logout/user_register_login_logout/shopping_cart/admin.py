from django.contrib import admin

from user_register_login_logout.shopping_cart.models import OrderItem, ShoppingCart


# Register your models here.
@admin.register(OrderItem)
class ModelNameAdmin(admin.ModelAdmin):
    pass


@admin.register(ShoppingCart)
class ModelNameAdmin(admin.ModelAdmin):
    pass
