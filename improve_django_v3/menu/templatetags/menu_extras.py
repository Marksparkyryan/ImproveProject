import datetime

from django.db.models import Min, Max
from django.db.models import Min
from django import template

from ..models import Menu

register = template.Library()


@register.simple_tag()
def menu_years(query):
    """Retrieve lowest expiration year in all menu objects, then create 
    and return a range of years from then up to now
    """
    if query.exists():
        years = query.aggregate(
            lowest_year=Min('expiration_date'),
            highest_year=Max('expiration_date'),
        )
        menu_years = [year for year in range(
            years['lowest_year'].year, years['highest_year'].year)]
    else:
        menu_years = None
    return menu_years

