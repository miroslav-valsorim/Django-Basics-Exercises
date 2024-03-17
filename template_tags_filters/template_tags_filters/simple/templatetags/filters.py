from django import template

register = template.Library()


def only_with_condition(numbers, condition_func):
    return [x for x in numbers if condition_func(x)]


@register.filter
def only_odd(numbers):
    return only_with_condition(numbers, lambda number: number % 2 > 0)


@register.filter
def only_even(numbers):
    return only_with_condition(numbers, lambda number: number % 2 == 0)
