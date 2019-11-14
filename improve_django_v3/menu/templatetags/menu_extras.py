import datetime
from django.db.models import Min
from django import template

from ..models import Menu

register = template.Library()


@register.simple_tag(name='menu_years')
def menu_years():
    """Retrieve lowest expiration year in all menu objects, then create 
    and return a range of years from then up to now
    """
    query = Menu.objects.values(
        'expiration_date'
    ).aggregate(
        lowest=Min('expiration_date')
    )
    lowest = int(query['lowest'].strftime('%Y'))    
    print(lowest)
    highest = int(datetime.datetime.now().strftime('%Y'))
    print(highest)
    years = [x for x in range(lowest, highest + 1)]
    return years
