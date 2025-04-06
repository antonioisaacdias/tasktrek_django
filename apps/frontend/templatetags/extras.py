from django import template

register = template.Library()

@register.filter
def until(value, max_val):
    return range(value, max_val)