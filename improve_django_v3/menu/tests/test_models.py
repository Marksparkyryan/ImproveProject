import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from ..models import Menu, Item, Ingredient


class MenuModelTests(TestCase):
    def setUp(self):
        user1 = User.objects.create(
            username="Sparky",
            password="password"
        ) 
        pepperoni = Ingredient.objects.create(
            name="Pepperoni"
        )
        pizza = Item.objects.create(
            name="Pizza4life",
            description="This is a pepperoni pizza",
            chef=user1,
            standard=True,
        )
        pizza.ingredients.add(pepperoni)
        spring_menu = Menu.objects.create(
            season="Spring 2019",
            expiry=datetime.date(year=2099, month=1, day=1)
        )
        spring_menu.items.add(pizza)
    
    def test_str_method(self):
        menu = Menu.objects.get(id=1)
        self.assertEqual(str(menu), menu.season)


class ItemModelTests(TestCase):
    def setUp(self):
        user1 = User.objects.create(
            username="Sparky",
            password="password"
        ) 
        pepperoni = Ingredient.objects.create(
            name="Pepperoni"
        )
        pizza = Item.objects.create(
            name="Pizza4life",
            description="This is a pepperoni pizza",
            chef=user1,
            standard=True,
        )
        pizza.ingredients.add(pepperoni)
        spring_menu = Menu.objects.create(
            season="Spring 2019",
            expiry=datetime.date(year=2099, month=1, day=1)
        )
        spring_menu.items.add(pizza)
    
    def test_str_method(self):
        item = Item.objects.get(id=1)
        self.assertEqual(str(item), item.name)


class IngredientModelTests(TestCase):
    def setUp(self):
        user1 = User.objects.create(
            username="Sparky",
            password="password"
        ) 
        pepperoni = Ingredient.objects.create(
            name="Pepperoni"
        )
        pizza = Item.objects.create(
            name="Pizza4life",
            description="This is a pepperoni pizza",
            chef=user1,
            standard=True,
        )
        pizza.ingredients.add(pepperoni)
        spring_menu = Menu.objects.create(
            season="Spring 2019",
            expiry=datetime.date(year=2099, month=1, day=1)
        )
        spring_menu.items.add(pizza)
    
    def test_str_method(self):
        ingredient = Ingredient.objects.get(id=1)
        self.assertEqual(str(ingredient), ingredient.name)
        