from django.shortcuts import render
from django.views import View
from datetime import date,timedelta
# Create your views here.
from .models import Order,ReserverDay
from tables.models import Table
from .forms import ReserverDayForm

def compute_date(date_query,day,tommorow=False):
	if tommorow:
		return date_query+day
	else:
		yes_day = date_query-day
		if yes_day<=date.today():
			return False
		return yes_day

class ReserverDayViews(View):
	model = ReserverDay
	template_name = "reserve_view.html"
	def get(self, request, *args, **kwargs):
		date_query = request.GET.get("date")
		date_form = ReserverDay()
		day = timedelta(days=1)
		if date_query:
			date_query = date(date_query)
			yesterday = compute_date(date_query,day)
			tommorow = compute_date(date_query,day,True)
			date_form.date = date_query
		else:
			yesterday = False
			date_form.date = date.today()
			tommorow = compute_date(date.today(),day,True)
		tables = Table.objects.all()
		context = {
			'title':'Reserve day',
			'tables': tables,
			'back':yesterday,
			'next':tommorow,
		}
		return render(request,self.template_name,context) 