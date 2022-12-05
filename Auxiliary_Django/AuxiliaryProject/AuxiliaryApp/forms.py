from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class userForm(UserCreationForm):
    password1 = forms.CharField(
        max_length=30, widget=forms.PasswordInput(
            attrs={
                    'class': 'form-control',
                    'placeholder':'Password'
					}
                )
            )
    password2 = forms.CharField(
        max_length=30, widget=forms.PasswordInput(
            attrs={
                    'class': 'form-control',
                    'placeholder':'Password'
					}
                )
            )

    class Meta:
        model= CustomUser
        fields = ['username','password1','password2','first_name','last_name','email','userType']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'your username'
                    }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'your firstname'
                    }
            ), 
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'your lastname'
                    }
            ), 
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'your email'
                    }
            ), 
            'userType': forms.Select(
                attrs={
                    'class': 'form-control',
                    }
            ), 
            
         }

class itemsForm(forms.ModelForm):
    class Meta:
        model= itemsDB
        fields = ['item_name','item_unit','item_quantity']
        widgets = {
            'item_name': forms.Select(
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

class vehiclesForm(forms.ModelForm):
    class Meta:
        model = vehicleDB
        fields = ['req_name', 'passengers','destination', 'purpose','date']
        widgets = {
            'req_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Juan Dela Cruz'
                    }
            ), 
            'passengers': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: 4'
                    }
            ), 
            'destination': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: TUP Manila'
                    }
            ), 
            'purpose': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Meeting'
                    }
            ), 
            'date': forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'type':'date'
                        }
                ),

        }