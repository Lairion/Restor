from django import template
from datetime import date,timedelta,datetime
from dateutil import parser
from orders.models import Order
from ..models import Table
register = template.Library()

@register.filter
def is_reserved(value,date): # Only one argument.
    table_id = int(value)
    date_query = parser.parse(date).date()
    orders = Order.objects.filter(
        tables__pk=table_id,
        reserve_day__date_reserver = date_query)
    if orders.exists():
        return True
    return False