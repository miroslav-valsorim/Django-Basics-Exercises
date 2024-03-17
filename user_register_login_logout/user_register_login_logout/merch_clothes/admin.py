from django.contrib import admin

from user_register_login_logout.merch_clothes.models import OrderClothes


# Register your models here.

@admin.register(OrderClothes)
class ModelNameAdmin(admin.ModelAdmin):
    pass