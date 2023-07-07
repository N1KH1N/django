from django.db import models
class Products(models.Model):
    name=models.CharField(max_length=50)
    price=models.PositiveIntegerField(null=True)
    category=models.CharField(max_length=20)
    description=models.CharField(max_length=50)
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Products.objects.create(name="logitech",price=1699,category="accessories",description="keyboard")


# fetch all objects
# qs=Modelsname.object.all()
# qs=Products.objects.all()

