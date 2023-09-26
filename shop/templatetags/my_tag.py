import datetime
import os

from django import template
from django.conf import settings
from django.contrib.auth.models import Group

register = template.Library()


# Создание фильтра
#@register.filter()
#def mediapath(val):
    #if val:
        #return f'/media/{val}'
    #return ''


@register.simple_tag
def mediapath(path):
    return os.path.join('/', settings.MEDIA_URL, str(path))
