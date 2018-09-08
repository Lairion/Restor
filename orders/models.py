from django.db import models

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
    number = models.IntegerField(unique=True)
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

    class Meta:
        pass