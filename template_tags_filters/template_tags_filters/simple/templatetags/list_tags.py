import datetime

from django import template
from django.template.defaultfilters import safe

register = template.Library()


# expects to return a HTML string
@register.simple_tag
def list_of(values):
    items_string = ''.join(f"<li>{value}</li>" for value in values)
    return safe(f"<ul>{items_string}</ul>")


@register.simple_tag
def current_time():
    return datetime.datetime.now()

# expects to return an HTML string based on template
# @register.inclusion_tag()
# def list_tags():
#     pass

# expects to return template Node 'render' func
# @register.tag()
