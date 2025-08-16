from django.db import models
from django.contrib.auth.models import User 
from menu.models import Menu 

# Create your models here.

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('confirmed','Confirmed'),
        ('delivered','Delivered'),
        ('cancelled','Cancelled'),
    )

    customer = models.ForeignKey(User, on_delete = models.CASCADE,related_name="orders")
    order_items = models.ManyToManyField(Menu,related_name="orders")
    total_amount = models.DecimalField(max_digits = 10,decimal_places = 2)
    status = models.CharField(max_legth = 20,choices=STATUS_CHOICES,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order {self.id} by {self.customer.username}"