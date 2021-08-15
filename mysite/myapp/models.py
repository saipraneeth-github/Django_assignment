
from django.db import models


#Categories
class Categories(models.Model):
   name = models.CharField(max_length=20, null=False)
   def __str__(self):
       return self.name

#Size
class Size(models.Model):
   category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
   size = models.IntegerField(null=False)
   def __str__(self):
       return self.size

#Products
class Products(models.Model):
    name = models.CharField(max_length=20, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2,null=False)
    description = models.TextField(max_length=2000, null=False)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

#ProductSize
class ProductSize(models.Model):
   product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
   size_id = models.ForeignKey(Size, on_delete=models.CASCADE)

#ProductImages
class Product_Images(models.Model):
   product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
   image_name = models.CharField(max_length = 20, null= False)
   def __str__(self):
       return self.image_name

'''
class Position(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100, null=False)
    emp_code = models.CharField(max_length=5, null=False)
    mobile = models.CharField(max_length=15, null=False)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
'''
