import datetime

from django.db.models import Min, Max
from django.db.models import Min
from django import template

from ..models import Menu

register = template.Library()

YEARS = [str(year) for year in range(2011, (datetime.datetime.now().year + 1))]


@register.simple_tag()
def menu_years():
    """Return range of menu expiration years"""
    return YEARS
