from datetime import datetime
# import pytz

from django.core.urlresolvers import reverse
from django.db.models import Min, Max, Prefetch
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone
from operator import attrgetter

from django.core.exceptions import ObjectDoesNotExist
from .models import Menu, Item, Ingredient
from .forms import  MenuCreateUpdateForm, MenuSearchForm


def menu_list(request):
    """Display all menus and items related to each menu ordered by 
    expiration date 
    """
    menus = Menu.objects.prefetch_related(
        Prefetch('items', queryset=Item.objects.all().only('name'))
    )[:9]
    context = {
        'menus': menus,
        'searchform': MenuSearchForm()
    }
    return render(request, 'menu/list_all_current_menus.html', context)


def menu_detail(request, pk):
    """Fetch menu based on passed in pk and prefetch items within menu
    """
    menu = Menu.objects.filter(
        pk=pk
    ).prefetch_related(
        'items'
    ).first()
    context = {
        'menu': menu,
        'searchform': MenuSearchForm()
    }
    return render(request, 'menu/menu_detail.html', context)


def item_detail(request, item_pk, menu_pk):
    """Fetch item details and prefetch the ingredients and select the 
    related chef as well 
    """
    item = Item.objects.filter(
        pk=item_pk
    ).prefetch_related(
        'ingredients'
    ).select_related(
        'chef'
    ).first()

    menu = Menu.objects.filter(
        pk=menu_pk
        ).values(
            'season',
            'id'
        ).first()

    context = {
        'item': item,
        'menu': menu,
        'searchform': MenuSearchForm()
    }
    return render(request, 'menu/detail_item.html', context)


def create_new_menu(request):
    """Provide unbound MenuCreateUpdateForm
    """
    form = MenuCreateUpdateForm()
    if request.method == "POST":
        form = MenuCreateUpdateForm(request.POST)
        if form.is_valid():
            menu = form.save()
            return redirect(reverse('menu:menu_detail', kwargs={'pk': menu.id }))
    context = {
        'form': form,
        'searchform': MenuSearchForm()
    }
    return render(request, 'menu/menu_create_update.html', context)


def edit_menu(request, pk):
    menu = Menu.objects.filter(
        id=pk
        ).prefetch_related(
            'items'
        ).first()
    form = MenuCreateUpdateForm(instance=menu)
    if request.method == 'POST':
        form = MenuCreateUpdateForm(data=request.POST, instance=menu)
        if form.is_valid():
            menu = form.save()
            return redirect(reverse('menu:menu_detail', kwargs={'pk': pk}))
    context = {
        'form': form,
        'menu': menu,
        'searchform': MenuSearchForm()
    }
    return render(request, 'menu/menu_create_update.html', context)


def menu_search(request):
    if request.method == 'GET':
        searchform = MenuSearchForm(request.GET)
        if searchform.is_valid():
            query = searchform.cleaned_data['q']
            menus = Menu.objects.filter(
                season__icontains=query
            ).prefetch_related(
                'items'
            )
            context = {
                'menus': menus,
                'searchform': MenuSearchForm()
            }
            return render(request, 'menu/list_all_current_menus.html', context)
    return render(request, 'menu/list_all_current_menus.html', context)