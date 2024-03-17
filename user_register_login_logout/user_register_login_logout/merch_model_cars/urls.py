from django.urls import path

from user_register_login_logout.merch_model_cars.views import ListModelCarsView, DetailModelCarsView

urlpatterns = (
    path('model_cars/', ListModelCarsView.as_view(), name="list_model_cars"),
    path('model_cars/detail/<slug:slug>/', DetailModelCarsView.as_view(), name="detail_model_car"),
)