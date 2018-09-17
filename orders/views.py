from django.shortcuts import render,redirect
from django.views import View
from datetime import date,timedelta,datetime
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context

# Create your views here.
from .models import Order,ReserverDay
from tables.models import Table
from .forms import ReserverDayForm,OrderForm
from dateutil import parser


def compute_date(date_query,day,tommorow=False):
    if tommorow:
        return date_query+day
    else:
        yes_day = date_query-day
        comp = (yes_day - date.today())
        if comp.days<0:
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
            date_query = str(date.today())
            date_form = self.form_class({"date_reserver":date.today()}) 
            yesterday = False
            tommorow = compute_date(date.today(),day,True)
        tables = Table.objects.all()
        order_form = OrderForm()
        context = {
            "date_query":date_query,
            'title':'Reserve day',
            'tables': tables,
            'back':yesterday,
            'next':tommorow,
            'date_form':date_form,
            'order_form':order_form 
        }
        return render(request,self.template_name,context)

    def post(self,request,*args, **kwargs):
        dict_form = request.POST.copy()
        date_query = dict_form.get("date_reserver")
        date_query = parser.parse(date_query).date()
        reserve_day_obj = ReserverDay.objects.get_or_create(date_reserver=date_query)
        dict_form["reserve_day"]=str(reserve_day_obj[0].id)
        order_form = OrderForm(dict_form)
        orders = Order.objects.filter(
            tables__pk__in=[int(i) for i in dict_form["tables"]],
            reserve_day__date_reserver = date_query
        )
        if order_form.is_valid and not orders.exists() :
            order_form.save()
            
        return redirect("/reserve_day/?date_reserver="+str(date_query))