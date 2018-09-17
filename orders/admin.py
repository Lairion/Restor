from django.contrib import admin
from .models import Order, ReserverDay
from .forms import OrderFormAdmin

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    '''
        Admin View for Order
    '''
    form = OrderFormAdmin

admin.site.register(Order, OrderAdmin)
admin.site.register(ReserverDay)
