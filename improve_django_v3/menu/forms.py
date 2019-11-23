from django import forms
from django.forms.extras.widgets import SelectDateWidget

from .models import Menu, Item, Ingredient

class MenuCreateUpdateForm(forms.ModelForm):

    season = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(attrs={
            'placeholder': "What's the season?",
        }))
    items = forms.ModelMultipleChoiceField(
        queryset=Item.objects.all(),
        required=False # setting to false to gain control of error msg
    )
    expiry = forms.DateField(input_formats=['%Y-%m-%d'], required=False,)

    class Meta:
        model = Menu
        exclude = ('created_date',)
    
    def clean_items(self):
        data = self.cleaned_data['items']
        if not data:
            raise forms.ValidationError("Menus need at least one item added.")
        return data


class MenuSearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        max_length=48,
        widget=forms.TextInput(attrs={
            'placeholder': "Search all menus",
        }))
    
    def clean_q(self):
        data = self.cleaned_data['q']
        if not data:
            raise forms.ValidationError("What are you searching for?")
        return data



