from django import forms
from django.forms.extras.widgets import SelectDateWidget

from .models import Menu, Item, Ingredient

class MenuForm(forms.ModelForm):

    items = forms.ModelMultipleChoiceField(
        queryset=Item.objects.all(),
        required=False,
        
    )

    class Meta:
        model = Menu
        exclude = ('created_date',)