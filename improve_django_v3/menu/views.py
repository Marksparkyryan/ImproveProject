from datetime import datetime
# import pytz

from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone
from operator import attrgetter

from django.core.exceptions import ObjectDoesNotExist
from .models import Menu, Item, Ingredient
from .forms import  MenuForm


def menu_list(request):
    """Display all menus and items related to each menu ordered by 
    expiration date 
    """
    menus = Menu.objects.all().prefetch_related(
        'items'
    ).order_by(
        'expiration_date',
    )
    return render(request, 'menu/list_all_current_menus.html', {'menus': menus})


def menu_detail(request, pk):
    """Fetch menu based on passed in pk and prefetch items within menu
    """
    menu = Menu.objects.filter(
        pk=pk
    ).prefetch_related(
        'items'
    ).first()
    return render(request, 'menu/menu_detail.html', {'menu': menu})


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
    }
    return render(request, 'menu/detail_item.html', context)


def create_new_menu(request):
    form = MenuForm(request.POST)
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.created_date = timezone.now()
            menu.save()
            return redirect('menu_detail', pk=menu.pk)
    
    return render(request, 'menu/menu_edit.html', {'form': form})


def edit_menu(request, pk):
    menu = Menu.objects.get(pk=pk)
    form = MenuForm(instance=menu)
    if request.method == 'POST':
        form = MenuForm(data=request.POST, instance=menu)
        print(form.data)
        if form.is_valid():
            cleaned = form.cleaned_data
            menu = form.save(commit=False)
            menu.save()
            return redirect(reverse('menu:menu_detail', kwargs={'pk': pk}))
    context = {
        'form': form,
        'menu': menu,
    }
    print(form.data)
    return render(request, 'menu/menu_edit.html', context)

    # menu = get_object_or_404(Menu, pk=pk)
    # items = Item.objects.all()
    # if request.method == "POST":
    #     menu.season = request.POST.get('season', '')
    #     menu.expiration_date = datetime.strptime(request.POST.get('expiration_date', ''), '%m/%d/%Y')
    #     menu.items = request.POST.get('items', '')
    #     menu.save()

    # return render(request, 'menu/menu_edit.html', {
    #     'menu': menu,
    #     'items': items,
    #     })
