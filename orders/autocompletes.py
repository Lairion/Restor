from dal import autocomplete

from .models import ReserverDay


class ReserverDayAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !

        qs = ReserverDay.objects.all()
        print(qs)
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
    def get_selected_result_label(self, item):
        return item.date_reserver

    def get_result_label(self, item):
        return item.date_reserver

