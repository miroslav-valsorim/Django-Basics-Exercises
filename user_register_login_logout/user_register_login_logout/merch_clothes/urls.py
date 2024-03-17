from django.urls import path

from user_register_login_logout.merch_clothes.views import ListClothesView, DetailClothesView

urlpatterns = (
    # path('', list_clothes, name='list_clothes'),
    path('clothes/', ListClothesView.as_view(), name="list_clothes"),
    path('clothes/detail/<slug:slug>/', DetailClothesView.as_view(), name="detail_clothes"),
)