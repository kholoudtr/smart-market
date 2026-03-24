from collections import UserDict
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
      name=models.CharField(max_length=50)
      description=models.TextField()
      image=models.ImageField(upload_to='photo/%y/%m/%d')
      def __str__(self):
            return self.name
      

class Product(models.Model):
      name=models.CharField(max_length=50)
      description=models.TextField()
      image=models.ImageField(upload_to='photo/%y/%m/%d')
      price=models.DecimalField(max_digits=8,decimal_places=4)
      date=models.DateField(auto_now_add=True)
      active=models.BooleanField(default=True)
      category=models.ForeignKey(Category,on_delete=models.CASCADE)
      def __str__(self):
            return self.name
      
# 
class Cart(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      product=models.ForeignKey(Product,on_delete=models.CASCADE)
      quantity=models.PositiveIntegerField(default=1)
      add_at=models.DateTimeField(auto_now_add=True)
      def __str__(self):
          return f"{self.user.username} - {self.product.name} × {self.quantity}"

      