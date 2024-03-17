from django.urls import path

from shopping_cart.product.views import DetailProductView, CategoryView, ListProductsView, ListTicketsView

urlpatterns = (
    path('', ListProductsView.as_view(), name="list_products"),
    # path('<slug:slug>/', list_products, name="list_products"),
    path('categories/', CategoryView.as_view(), name="product_categories"),
    path('tickets/', ListTicketsView.as_view(), name="product_tickets"),
    path('detail/<slug:slug>/', DetailProductView.as_view(), name="detail_product"),
)