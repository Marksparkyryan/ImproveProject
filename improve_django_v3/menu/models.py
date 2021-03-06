from django.contrib.auth.models import User
from django.db import models


class Menu(models.Model):
    """Model representing a Menu that contains Items
    """
    season = models.CharField(max_length=20)
    items = models.ManyToManyField('Item', related_name='items')
    created = models.DateField(auto_now_add=True, null=True)
    expiry = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.season


class Item(models.Model):
    """Model representing an Item that contains Ingredients
    """
    name = models.CharField(max_length=200)
    description = models.TextField()
    chef = models.ForeignKey(User)
    created = models.DateField(auto_now_add=True, null=True)
    standard = models.BooleanField(default=False)
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Model representing an Ingredient 
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
