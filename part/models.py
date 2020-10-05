from django.db import models

class PartModel(models.Model):
    part_id=models.AutoField(primary_key=True)
    description=models.CharField("Part Description", max_length=250)
    part_code=models.CharField("Part Code", max_length=15,unique=True)

    def __str__(self):
        return self.part_code+" "+self.description
