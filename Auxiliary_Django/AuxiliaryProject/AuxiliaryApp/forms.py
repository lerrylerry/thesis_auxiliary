from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from AuxiliaryApp.models import itemsDB


class itemsForm(forms.ModelForm):
    class Meta:
        model= itemsDB
        fields = ['item_name','item_unit','item_quantity']
        widgets = {
            'item_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Round Rags'
                    }
            ),
            'item_unit': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: pcs'
                    }
            ), 
            'item_quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: 5'
                    }
            ), 
         }