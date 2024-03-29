from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic as views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from shopping_cart.cart_order.models import OrderItem, ShoppingCart
from shopping_cart.product.models import Products


# Create your views here.
@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Products, slug=slug)

    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False,
    )
    order_qs = ShoppingCart.objects.filter(
        user=request.user,
        ordered=False
    )
    print(order_qs)
    print(order_item)
    print(created)
    print(item)
    print(request.session)
    print(request)
    for key, value in request.session.items():
        print(key, value)
    print(request.COOKIES)

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")

        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart")
    else:
        ordered_date = timezone.now()
        order = ShoppingCart.objects.create(
            user=request.user,
            ordered_date=ordered_date,
        )
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")

    # return redirect("detail_product", slug=slug)
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Products, slug=slug)

    order_qs = ShoppingCart.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False,
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart")
        else:
            messages.info(request, "This item was not in your cart")
    else:
        messages.info(request, "You dont have active order")

    return redirect("cart_details")


@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Products, slug=slug)
    order_qs = ShoppingCart.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
                # order_item.delete()
            messages.info(request, "This item quantity was updated.")
            return redirect("cart_details")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("cart_details")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("cart_details")


@login_required
def add_single_item_to_cart(request, slug):
    item = get_object_or_404(Products, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False,
    )
    order_qs = ShoppingCart.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")

        else:
            messages.info(request, "This item was added to your cart")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = ShoppingCart.objects.create(
            user=request.user,
            ordered_date=ordered_date,
        )
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")

    return redirect("cart_details")


class ShoppingCartSummary(LoginRequiredMixin, views.View):
    def get(self, *args, **kwargs):
        try:
            order = ShoppingCart.objects.get(user=self.request.user, ordered=False)
            context = {
                "object": order
            }
            return render(self.request, "cart/cart_details.html", context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You dont have an active order")
            return render(self.request, "cart/cart_details.html")

        # return render(self.request, 'cart/cart_details.html')
