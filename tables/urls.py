from django.urls import path, include
from .autocompletes import TableAutocomplete
urlpatterns = [
    path('table_autocomplete/',
        ReserverDayAutocomplete.as_view(),
        name='table_autocomplete',
    ),
]
