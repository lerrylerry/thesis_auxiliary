from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from AuxiliaryApp.models import itemsDB, janitorDB


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

class janitorForm(forms.ModelForm):
    class Meta:
        model = janitorDB
        fields = ['up_name','up_code','up_status']
        widgets = {
            'up_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Juan Dela Cruz'
                    }
            ),
            'up_code': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: 4325'
                    }
            ), 
            'up_status': forms.Select(
                attrs={
                    'class': 'form-control',
                    }
            ), 
         }
class borrowUPForm(forms.ModelForm):
    up_code = forms.CharField(
        max_length=4, widget=forms.PasswordInput(
            attrs={
                    'class': 'form-control',
                    'placeholder':'Pincode'
					}
                )
            )
    class Meta:
        model = janitorDB
        fields = ['up_name', 'up_code']
        widgets = {
            'up_name': forms.Select(
                attrs={
                    'class': 'form-control',
                    }
            ), 
        }