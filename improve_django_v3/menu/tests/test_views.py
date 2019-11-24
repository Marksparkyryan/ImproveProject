import datetime 

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from ..models import Menu, Item, Ingredient


class MenuListTests(TestCase):
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
    
    def test_menu_list_menu_search(self):
        resp = self.client.get(reverse('menu:home'))
        self.assertEquals(resp.status_code, 200)
        self.assertContains(resp, "Pizza4life")
        self.assertEqual(len(resp.context['menus']), 1)
        self.assertTemplateUsed(resp, 'menu/base.html')
        self.assertTemplateUsed(resp, 'menu/list_all_current_menus.html')
    
    def test_menu_list_expired(self):
        resp = self.client.get(
            reverse('menu:menu_list', kwargs={'query': 'expired'})
            )
        self.assertEquals(resp.status_code, 200)
        self.assertContains(resp, "No menus found!")
        self.assertEqual(len(resp.context['menus']), 0)
        self.assertTemplateUsed(resp, 'menu/base.html')
        self.assertTemplateUsed(resp, 'menu/list_all_current_menus.html')

    def test_menu_list_fresh(self):
        resp = self.client.get(
            reverse('menu:menu_list', kwargs={'query': 'fresh'})
            )
        self.assertEquals(resp.status_code, 200)
        self.assertContains(resp, "Pizza4life")
        self.assertEqual(len(resp.context['menus']), 1)
        self.assertTemplateUsed(resp, 'menu/base.html')
        self.assertTemplateUsed(resp, 'menu/list_all_current_menus.html')
    
    def test_menu_list_2100(self):
        resp = self.client.get(
            reverse('menu:menu_list', kwargs={'query': '2100'})
            )
        self.assertEquals(resp.status_code, 200)
        self.assertContains(resp, "No menus found!")
        self.assertEqual(len(resp.context['menus']), 0)
        self.assertTemplateUsed(resp, 'menu/base.html')
        self.assertTemplateUsed(resp, 'menu/list_all_current_menus.html')
    
    def test_menu_list_2099(self):
        resp = self.client.get(
            reverse('menu:menu_list', kwargs={'query': '2099'})
            )
        self.assertEquals(resp.status_code, 200)
        self.assertEqual(len(resp.context['menus']), 1)
        self.assertTemplateUsed(resp, 'menu/base.html')
        self.assertTemplateUsed(resp, 'menu/list_all_current_menus.html')
    
    def test_menu_list_all(self):
        resp = self.client.get(
            reverse('menu:menu_list', kwargs={'query': 'all'})
            )
        self.assertEquals(resp.status_code, 200)
        self.assertEqual(len(resp.context['menus']), 1)
        self.assertTemplateUsed(resp, 'menu/base.html')
        self.assertTemplateUsed(resp, 'menu/list_all_current_menus.html')
    

class MenuDetailTests(TestCase):
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

    def menu_detail_no_pk(self):
        resp = self.client.get(reverse('menu:menu_detail'))
        self.assertEqual(resp.status_code, 404)
    
    def test_detail_with_pk(self):
        resp = self.client.get(
            reverse('menu:menu_detail', kwargs={'pk': 1})
        )
        self.assertEquals(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/menu_detail.html')
        self.assertIsInstance(resp.context['menu'], Menu)
        self.assertContains(resp, 'Pizza4life')
        self.assertContains(resp, 'Spring 2019')
    
    
class ItemDetailTests(TestCase):
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
    

    def test_item_detail_with_pks(self):
        resp = self.client.get(
            reverse(
                'menu:item_detail', 
                kwargs={
                    'item_pk': 1,
                    'menu_pk': 1
                    }))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/detail_item.html')
        self.assertIsInstance(resp.context['item'], Item)
        self.assertEqual(resp.context['menu']['season'], 'Spring 2019')
        self.assertContains(resp, 'Spring 2019')
        self.assertContains(resp, 'Pepperoni')
        self.assertContains(resp, 'Standard Item')
        self.assertContains(resp, 'Sparky')


class CreateNewMenuTests(TestCase):
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

    def test_adding_menu(self):
        resp = self.client.post(
            reverse('menu:menu_new'), data={
                'season': 'Fall 2020',
                'items': [1, ],
                'expiry': datetime.date(year=2020, month=12, day=31),
                'chef': 1
            },
            follow=True
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/menu_detail.html')
        self.assertContains(resp, 'Fall 2020')
    
    def test_adding_menu_blank(self):
        resp = self.client.get(reverse('menu:menu_new'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/menu_create_update.html')


class EditMenuTests(TestCase):
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
            expiry=datetime.date(year=2099, month=1, day=1),
        )
        spring_menu.items.add(pizza)
    
    def test_edit_with_pk_get(self):
        resp = self.client.get(
            reverse('menu:menu_edit', kwargs={'pk': 1})
            )
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/menu_create_update.html')
    
    def test_edit_with_pk_post(self):
        resp = self.client.post(
            reverse('menu:menu_edit',
                    kwargs={'pk': 1}),
            data={
                'season': 'NewSpring',
                'items': 1,
                'expiry': datetime.date(year=1929, month=1, day=1)
            },
            follow=True
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'menu/menu_detail.html')
        self.assertContains(resp, 'NewSpring')
        self.assertEqual(resp.context['menu'].id, 1)
        self.assertEqual(
            resp.context['menu'].expiry,
            datetime.date(year=1929, month=1, day=1)
        )

    def test_edit_with_bad_pk(self):
        resp = self.client.get(
            reverse('menu:menu_edit', kwargs={'pk': 99}))
        self.assertEqual(resp.status_code, 200)
        

class MenuSearchTests(TestCase):
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
            season="Spring 2021",
            expiry=datetime.date(year=2099, month=1, day=1)
        )
        spring_menu.items.add(pizza)
    
    def test_search(self):
        resp = self.client.get('/menu/search/', data={'q': 'Spring'})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Spring 2021')
        self.assertTemplateUsed(resp, 'menu/list_all_current_menus.html')
        self.assertEqual(len(resp.context['menus']), 1)
    
    def test_bad_search(self):
        resp = self.client.get('/menu/search/', data={'q': 'Mississauga'})
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'No menus found!')
        self.assertTemplateUsed(resp, 'menu/list_all_current_menus.html')
        self.assertEqual(len(resp.context['menus']), 0)
    
    def test_good_search(self):
        resp = self.client.get('/menu/search/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'No menus found!')
        self.assertTemplateUsed(resp, 'menu/list_all_current_menus.html')
        self.assertEqual(resp.context['menus'], None)
