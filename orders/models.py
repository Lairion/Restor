from django.db import models
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
# Create your models here.
class ReserverDay(models.Model):
    """
    Description: Model Description
    """
    date_reserver = models.DateField()
    
    class Meta:
        ordering = ("-date_reserver",)

    def __str__(self):
        return str(self.date_reserver)

class Order(models.Model):
    """
    Description: Model Description
    """
    tables = models.ManyToManyField(
        'tables.Table', 
        related_name='orders'
        )
    reserve_day = models.ForeignKey(
        'ReserverDay', 
        on_delete=models.PROTECT,
        related_name='orders_today'
        )
    email_customer=models.CharField(max_length=100)
    customer_name=models.CharField(max_length=100)

    def __str__(self):
        return str(self.number)
    
    def save(self, *args, **kwargs):
        
        ret = super(Order, self).save(*args, **kwargs)
        send_mail(
            'Thanks for order!',
            get_template('email/thanks_for_order.html').render({
                    'username': self.customer_name,
                    'number': self.id
                }
            ),
            'admin@example.com',
            [self.email_customer],
            fail_silently = True
        )
        return ret

    class Meta:
        pass