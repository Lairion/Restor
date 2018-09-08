from django.contrib import admin
from .models import Table
# Register your models here.

class TableAdmin(admin.ModelAdmin):
    '''
        Admin View for Table
    '''
    list_display = ('number',)
    list_filter = ('number',)

admin.site.register(Table, TableAdmin)
