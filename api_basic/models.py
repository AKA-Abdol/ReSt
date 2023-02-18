from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title} by {self.author}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    def __str__(self) -> str:
        return f'{self.title} with {self.price} price'

    @property
    def sale_price(self):
        return float(self.price) * 0.85