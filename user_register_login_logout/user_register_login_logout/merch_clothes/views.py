from django.shortcuts import render

from user_register_login_logout.merch_clothes.models import OrderClothes
from django.views import generic as views


# Create your views here.

# #FBV
# def list_clothes(request):
#     context = {
#         'items': OrderClothes.objects.all()
#     }
#     return render(request,"merch_clothes/clothes_list.html", context)

# CBV
class ListClothesView(views.ListView):
    model = OrderClothes
    paginate_by = 2
    template_name = 'merch_clothes/clothes_list.html'


class DetailClothesView(views.DetailView):
    model = OrderClothes
    template_name = 'merch_clothes/clothes_details.html'
