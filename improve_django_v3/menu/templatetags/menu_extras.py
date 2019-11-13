import datetime
from django.db.models import Min
from django import template

from ..models import Menu

register = template.Library()


@register.simple_tag(takes_context=True, name='menu_years')
def menu_years(context):
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
