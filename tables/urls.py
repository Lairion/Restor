from django.urls import path, include
from .autocompletes import TableAutocomplete
urlpatterns = [
    path('table_autocomplete/',
        TableAutocomplete.as_view(),
        name='table_autocomplete',
    ),
]
