from django.urls import path, include
from .views import ReserverDayViews
from .autocompletes import ReserverDayAutocomplete
urlpatterns = [
    path('reserve_day/', ReserverDayViews.as_view(),name='reserve_day'),
    path('reserve_day_autocomplete/',
        ReserverDayAutocomplete.as_view(),
        name='reserver_day_autocomplete',
    ),
]
