from django.db import models

class Bikes(models.Model):
    name=models.CharField (max_length=200)
    model=models.CharField (max_length=200)
    price=models.PositiveIntegerField()
    kmdriven=models. PositiveIntegerField()
    description=models. CharField (max_length=200)
    image=models.ImageField (upload_to="images",null=True)
    def __str__(self):
        return self.name