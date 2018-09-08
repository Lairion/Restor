from django.db import models

# Create your models here.
class Table(models.Model):

    FORM_TYPE = (
        ('rectangle','Rectangle'),
        ('ellipse','Ellipse')
        )
    number = models.IntegerField()
    capacity = models.IntegerField()
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    form_type = models.CharField(
        max_length=50,
        choices=FORM_TYPE,
        default='rectangle'
    )
    height = models.FloatField()
    width = models.FloatField()

    class Meta:
        verbose_name = "Table"
        verbose_name_plural = "Tables"

    def __str__(self):
        return str(self.number)
    