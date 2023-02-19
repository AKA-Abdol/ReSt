from django.db import models

class Realty(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    sqft = models.IntegerField()
    garage = models.IntegerField(default=0)
    floor = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=11, decimal_places=10)

    def __str__(self) -> str:
        return f'Realty {self.title}, {self.sqft}ft, {self.price}$'

