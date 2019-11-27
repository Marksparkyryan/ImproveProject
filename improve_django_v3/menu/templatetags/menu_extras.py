import datetime

from django import template

register = template.Library()

YEARS = [str(year) for year in range(2011, (datetime.datetime.now().year + 1))]


@register.simple_tag()
def menu_years():
    """Return range of menu expiration years"""
    return YEARS
