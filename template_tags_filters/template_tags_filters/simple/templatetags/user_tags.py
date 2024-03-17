from django import template
from django.contrib.auth.models import User

register = template.Library()


@register.inclusion_tag('main_page/profile_avatar.html')
def profile_avatar():
    return {
        'user': 'Miro',
    }
