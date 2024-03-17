from django.urls import path

from shopping_cart.home_page.views import home_page

urlpatterns = (
    path("", home_page, name="home_page"),
)
