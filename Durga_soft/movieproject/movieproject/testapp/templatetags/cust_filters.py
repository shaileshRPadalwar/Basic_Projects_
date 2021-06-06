#filter to return "SHAILESH"
from django import template

register=template.Library()

@register.filter(name='truncate_3')
def truncate3(value):
    result=value[0:3]
    return result


@register.filter(name='truncate_n')
def truncate_n(value,n):
    result=value[0:n]
    return result