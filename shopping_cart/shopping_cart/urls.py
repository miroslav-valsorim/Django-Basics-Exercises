
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("shopping_cart.home_page.urls")),
    path('account/', include("shopping_cart.accounts.urls")),
    path('products/', include("shopping_cart.product.urls")),
    path('cart/', include("shopping_cart.cart_order.urls")),
    path('checkout/', include("shopping_cart.checkout.urls")),
    path('', include('paypal.standard.ipn.urls')),
]
