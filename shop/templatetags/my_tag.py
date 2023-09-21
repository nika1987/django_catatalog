import datetime
from django import template
from django.contrib.auth.models import Group

register = template.Library()


# Создание фильтра
@register.filter()
def mediapath(val):
    if val:
        return f'/media/{val}'
    return ''


@register.simple_tag()
def mediapath(val):
    if val:
        return f'/media/{val}'
    return ''
