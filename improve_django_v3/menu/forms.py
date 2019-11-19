from django import forms
from django.forms.extras.widgets import SelectDateWidget

from .models import Menu, Item, Ingredient

class MenuCreateUpdateForm(forms.ModelForm):

    items = forms.ModelMultipleChoiceField(
        queryset=Item.objects.all(),
        required=False,
    )
    expiry = forms.DateField(input_formats=['%Y-%m-%d'])

    class Meta:
        model = Menu
        exclude = ('created_date',)


class MenuSearchForm(forms.Form):
    q = forms.CharField(max_length=48, min_length=1)



