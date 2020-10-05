from django.db import models

class ColorModel(models.Model):
    color_id=models.AutoField(primary_key=True)
    name=models.CharField("Color Name", max_length=50)
    color_code=models.CharField("Color Code", max_length=5,unique=True)

    def __str__(self):
        return self.color_code+" "+self.name
