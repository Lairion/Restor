from dal import autocomplete

from .models import Table


class TableAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !

        qs = Table.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs