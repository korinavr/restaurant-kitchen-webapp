from django.db import models
from django.contrib.auth.models import User


# Create the database model
CATEGORIES = (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('main_dish', 'Main Dishes'),
    ('desert', 'Desert')
)


STATUS=(
    (0, 'Unavailable'),
    (1, 'Available')
)


class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, choices=CATEGORIES)
    status = models.IntegerField(choices=STATUS, default=1)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal