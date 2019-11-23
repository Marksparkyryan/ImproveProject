import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from ..forms import MenuCreateUpdateForm, MenuSearchForm
from ..models import Menu, Item, Ingredient

class MenuCreateFormTests(TestCase):
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

    def test_form_invalid(self):
        data = {
            'season': None,
            'items': None,
            'expiry': datetime.date.today()
        }
        form = MenuCreateUpdateForm(data=data)
        self.assertFalse(form.is_valid())
    
    def test_form_invalid_items(self):
        data = {
            'season': 'Spring2345',
            'items': None,
            'expiry': datetime.date.today()
        }
        form = MenuCreateUpdateForm(data=data)
        self.assertFalse(form.is_valid())
    
    def test_form_invalid_date(self):
        data = {
            'season': 'Spring2345',
            'items': [1],
            'expiry': "2019/01/01"
        }
        form = MenuCreateUpdateForm(data=data)
        self.assertFalse(form.is_valid())
    
    def test_form_valid(self):
        data = {
            'season': "Fall2020",
            'items': [1],
            'expiry': datetime.date.today()
        }
        form = MenuCreateUpdateForm(data=data)
        self.assertTrue(form.is_valid())


class MenuSearchFormTests(TestCase):
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
    
    def test_empty_search(self):
        data = {'q': None}
        form = MenuSearchForm(data=data)
        self.assertFalse(form.is_valid())

    def test_valid_search(self):
        data = {'q': 'pizza'}
        form = MenuSearchForm(data=data)
        self.assertTrue(form.is_valid())
    

