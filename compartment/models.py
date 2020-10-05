from django.db import models

class CompartmentModel(models.Model):
    compartment_id=models.AutoField(primary_key=True)
    name=models.CharField("compartment name", max_length=50)
    code=models.CharField("compartment code",max_length=5,unique=True)

    def __str__(self):
        return self.code+" "+self.name
