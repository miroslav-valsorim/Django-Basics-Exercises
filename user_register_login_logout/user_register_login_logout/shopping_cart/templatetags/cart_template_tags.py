from django import template

from user_register_login_logout.shopping_cart.models import ShoppingCart

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = ShoppingCart.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0
