from django.db import models
from compartment.models import CompartmentModel

class EmployeeModel(models.Model):
    employee_id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    compartment=models.ForeignKey(CompartmentModel,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.fname+" "+self.lname+" "+self.email
