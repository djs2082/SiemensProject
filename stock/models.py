from django.db import models
from django.utils import timezone
from compartment.models import CompartmentModel
from part.models import PartModel
from color.models import ColorModel


class StockModel(models.Model):
    compartment=models.ForeignKey(CompartmentModel, verbose_name="Compartment Name", on_delete=models.CASCADE)
    part=models.ForeignKey(PartModel, verbose_name="Part Name", on_delete=models.CASCADE)
    color=models.ForeignKey(ColorModel, verbose_name="Color Name", on_delete=models.CASCADE)
    quantity=models.IntegerField("Quantity",default=0)
    date=models.DateField("Date",default=timezone.now)

    def __str__(self):
        return self.compartment.name+" "+self.quantity+self.date

