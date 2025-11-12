from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class GroceryItem(models.Model):
    CATEGORY_CHOICES = [
        ('Produce', 'Produce'),
        ('Dairy', 'Dairy'),
        ('Meat', 'Meat'),
        ('Bakery', 'Bakery'),
        ('Pantry', 'Pantry'),
        ('Frozen', 'Frozen'),
        ('Beverages', 'Beverages'),
        ('Snacks', 'Snacks'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
