from django.db import models
from employee.models import EmployeeModel
from actions.models import ActionsModel

class ActionsTakenModel(models.Model):
    id=models.AutoField(primary_key=True)
    employee=models.ForeignKey(EmployeeModel, verbose_name="Employee Name", on_delete=models.SET_NULL,null=True)
    action=models.ForeignKey(ActionsModel, verbose_name="Action", on_delete=models.SET_NULL,null=True)
    date_time=models.DateTimeField("Date Time", auto_now_add=True,blank=True)

    def __str__(self):
        return self.action.name+" "+self.date_time

