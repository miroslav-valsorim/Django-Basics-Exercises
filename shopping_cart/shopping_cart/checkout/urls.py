from django.urls import path

from shopping_cart.checkout.views import CheckoutView, paypal_payment_successful, paypal_payment_failed, \
    PaymentView

urlpatterns = (
    path('', CheckoutView.as_view(), name='checkout'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('payment/success/<int:shopping_cart_id>/', paypal_payment_successful, name='paypal_payment_successful'),
    path('payment/failed/<int:shopping_cart_id>/', paypal_payment_failed, name='paypal_payment_failed'),
)
