import datetime
import os

from django import template
from django.conf import settings
from django.contrib.auth.models import Group
from django.template.defaultfilters import truncatechars

register = template.Library()


@register.filter
def mediapath(image_path):
    # Формируем полный путь к медиафайлу, добавляя префикс '/media/'
    media = settings.MEDIA_URL
    return f"{media}{image_path}"


@register.filter
def truncate_description(description, length=100):
    # Обрезаем описание до первых 100 символов
    return truncatechars(description, length)


@register.simple_tag
def mediapath(path):
    return os.path.join('/', settings.MEDIA_URL, str(path))
