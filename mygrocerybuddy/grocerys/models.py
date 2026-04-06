from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

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

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Other')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    complete = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
