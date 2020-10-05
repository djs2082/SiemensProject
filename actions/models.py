from django.db import models
from compartment.models import CompartmentModel

class ActionsModel(models.Model):
    action_id=models.AutoField(primary_key=True)
    name=models.CharField("Action Name", max_length=150)
    compartment=models.ForeignKey(CompartmentModel, verbose_name="Compartment Name", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
