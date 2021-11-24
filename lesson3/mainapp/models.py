from django.db import models

# Create your models here.
class ProductCategory (models.Model):
    name = models.CharField(max_length=64)
    discription = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'{self.name}'

class Product (models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='product_image', blank=True)
    discription = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantiti = models.PositiveIntegerField(default=8)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}|{self.category},'