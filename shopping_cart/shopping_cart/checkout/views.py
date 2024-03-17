from aiohttp.payload import Order
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic as views
from paypal.standard.forms import PayPalPaymentsForm
import uuid

from shopping_cart.cart_order.models import ShoppingCart, OrderItem
from shopping_cart.checkout.forms import CheckoutForm
from shopping_cart.checkout.models import BillingAddress


class CheckoutView(views.View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, 'checkout/checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = ShoppingCart.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data['street_address']
                apartment_address = form.cleaned_data['apartment_address']
                country = form.cleaned_data['country']
                zip = form.cleaned_data['zip']
                # same_shipping_address = form.cleaned_data['same_shipping_address']
                # save_info = form.cleaned_data['save_info']
                # payment_option = form.cleaned_data['payment_option']
                billing_address = BillingAddress(
                    user=self.request.user,
                    street_address=street_address,
                    apartment_address=apartment_address,
                    country=country,
                    zip=zip,
                )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                # return redirect("checkout")
                # if payment_option == 'Stripe':
                #     return redirect('payment', payment_option=payment_option)
                # elif payment_option == 'PayPal':
                #     return redirect('payment', payment_option=payment_option)
                return redirect('payment')

            messages.warning(self.request, 'Failed Checkout')
            return redirect("checkout")
        except ObjectDoesNotExist:
            messages.error(self.request, "You don't have active order")
            return redirect("shopping_cart")


class PaymentView(views.TemplateView):
    template_name = 'checkout/payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = get_object_or_404(ShoppingCart, user=self.request.user, ordered=False)
        host = self.request.get_host()

        paypal_checkout = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': order.get_total(),
            'item_name': order.id,
            'invoice': uuid.uuid4(),
            'currency_code': 'USD',
            'notify_url': f"http://{host}{reverse('paypal-ipn')}",
            'return_url': f"http://{host}{reverse('paypal_payment_successful', kwargs={'shopping_cart_id': order.id})}",
            'cancel_url': f"http://{host}{reverse('paypal_payment_failed', kwargs={'shopping_cart_id': order.id})}",
        }

        paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

        context['order'] = order
        context['paypal'] = paypal_payment
        return context


# class PaymentView(views.View):
#     def get(self, *args, **kwargs):
#         # order = ShoppingCart.objects.get(user=self.request, ordered=False)
#         # context = {
#         #     "order": order,
#         #
#         # }
#         return render(self.request, "checkout/payment.html")
#
#     # def post(self, *args, **kwargs):
#     #     return render(self.request, 'checkout/payment.html')

# def payment(request):
#     order = ShoppingCart.objects.get(user=request.user, ordered=False)
#     # print(order.get_total())
#     host = request.get_host()
#
#     paypal_checkout = {
#         'business': settings.PAYPAL_RECEIVER_EMAIL,
#         'amount': order.get_total(),
#         'item_name': order.id,
#         'invoice': uuid.uuid4(),
#         'currency_code': 'USD',
#         'notify_url': f"http://{host}{reverse('paypal-ipn')}",
#         'return_url': f"http://{host}{reverse('paypal_payment_successful', kwargs={'shopping_cart_id': order.id})}",
#         'cancel_url': f"http://{host}{reverse('paypal_payment_failed' , kwargs={'shopping_cart_id': order.id})}",
#     }
#
#     paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)
#
#     context = {
#         'order': order,
#         'paypal': paypal_payment,
#     }
#     return render(request, 'checkout/payment.html', context)


def paypal_payment_successful(request, shopping_cart_id):
    cart_id = ShoppingCart.objects.get(id=shopping_cart_id)
    order = ShoppingCart.objects.get(user=request.user, ordered=False)
    order.ordered = True
    order.save()

    order_items = order.items.all()
    order_items.update(ordered=True)
    for item in order_items:
        item.save()

    context = {
        'cart_id': cart_id.id,
    }

    return render(request, 'checkout/payment-success.html', context)


def paypal_payment_failed(request, shopping_cart_id):
    cart_id = ShoppingCart.objects.get(id=shopping_cart_id)

    context = {
        'cart_id': cart_id.id,
    }

    return render(request, 'checkout/payment-failed.html', context)
