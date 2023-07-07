from django.db import models


class Books(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=250)
    publisher=models.CharField(max_length=200)
    genre=models.CharField(max_length=220)
    isbn=models.CharField(max_length=200)
    published_date=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.name