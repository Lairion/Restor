from dal import autocomplete
from django import forms
from .models import Order,ReserverDay
from tables.models import Table
from bootstrap_datepicker.widgets import DatePicker
from django.conf import settings

  

class OrderForm(forms.ModelForm):

   
    class Meta:
        model = Order
        fields = ('__all__')
        widgets = {
            'reserve_day': forms.HiddenInput(),
            # autocomplete.ModelSelect2(
            #     url='reserver_day_autocomplete',
            #     attrs={'data-html': 'true'}
            #     ),
            # 'tables': autocomplete.ModelSelect2Multiple(
            #     url='table_autocomplete')
        }
    

class OrderFormAdmin(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')
        widgets = {
            'reserve_day': autocomplete.ModelSelect2(
                url='reserver_day_autocomplete',
                attrs={'data-html': 'true'}
                ),
            'tables': autocomplete.ModelSelect2Multiple(
                url='table_autocomplete')
        }
class ReserverDayForm(forms.ModelForm):
    class Meta:
        model = ReserverDay
        fields = ('__all__')
        widgets = {
            'date_reserver':DatePicker(
                options={
                    "format": "yyyy-mm-dd",
                    "autoclose": True
                }
            )
        }