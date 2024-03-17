from django.contrib import admin

from user_register_login_logout.merch_model_cars.models import OrderModelCars


# Register your models here.
@admin.register(OrderModelCars)
class ModelNameAdmin(admin.ModelAdmin):
    pass