from django import template

register = template.Library()

@register.filter
def split_string(value, delimiter=","):
    """Custom filter to split a string by a delimiter."""
    return value.split(delimiter)
