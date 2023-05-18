from django import forms
from .models import *


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
