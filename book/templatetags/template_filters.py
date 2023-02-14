# customized template for html
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return getattr(dictionary, key)