from django.contrib import admin

from shopping_cart.checkout.models import BillingAddress


# Register your models here.
@admin.register(BillingAddress)
class ModelNameAdmin(admin.ModelAdmin):
    pass
