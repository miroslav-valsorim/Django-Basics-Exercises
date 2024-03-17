from django.shortcuts import render
from django.views import generic as views

from user_register_login_logout.merch_model_cars.models import OrderModelCars


# Create your views here.
class ListModelCarsView(views.ListView):
    model = OrderModelCars
    paginate_by = 2
    template_name = 'merch_model_cars/model_cars_list.html'


class DetailModelCarsView(views.DetailView):
    model = OrderModelCars
    template_name = 'merch_model_cars/model_cars_details.html'
