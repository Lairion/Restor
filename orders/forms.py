from dal import autocomplete

from django import forms
from .models import Order,ReserverDay

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')
        widgets = {
            'reserve_day': autocomplete.ModelSelect2(
                url='reserver_day_autocomplete'
                ),
            'tables': autocomplete.ModelSelect2Multiple(
                url='table_autocomplete')
        }
class ReserverDayForm(forms.ModelForm):
    date = forms.DateField()