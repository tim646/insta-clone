import magic
from  django import template
register = template.Library()


@register.filter
def get_value(var):
    return var.split(',')[0][2:-1]
