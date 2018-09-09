from django.shortcuts import render
from django.views import View
from datetime import date,timedelta,datetime
from django.conf import settings
# Create your views here.
from .models import Order,ReserverDay
from tables.models import Table
from .forms import ReserverDayForm
from dateutil import parser


def compute_date(date_query,day,tommorow=False):
	if tommorow:
		return date_query+day
	else:
		yes_day = date_query-day

		comp = (yes_day - date.today())
		if comp.days<1:
			return False
		return yes_day

class ReserverDayViews(View):
	model = ReserverDay
	template_name = "reserve_view.html"
	form_class = ReserverDayForm
	def get(self, request, *args, **kwargs): 
		day = timedelta(days=1)
		date_form = self.form_class(request.GET)
		date_query = request.GET.get("date_reserver")
		if date_query:
			dt = parser.parse(date_query).date()
			yesterday = compute_date(dt,day)
			tommorow = compute_date(dt,day,True)
			date_form = self.form_class({"date_reserver":dt})
		else:
			date_form = self.form_class({"date_reserver":date.today()})	
			yesterday = False
			tommorow = compute_date(date.today(),day,True)
		tables = Table.objects.all()
		context = {
			'title':'Reserve day',
			'tables': tables,
			'back':yesterday,
			'next':tommorow,
			'date_form':date_form
		}
		return render(request,self.template_name,context) 