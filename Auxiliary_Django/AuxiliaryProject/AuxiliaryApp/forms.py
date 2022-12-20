from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

USERTYPE = [
        ('','Select user here'),
        ('ADMIN','ADMIN'),
        ('ASSISTANT_DIRECTOR','ASSISTANT_DIRECTOR'),
    ]

USER_A = [
    ('','Select user here'),
    ('ADMIN','ADMIN'),
]

USER_B = [
    ('','Select user here'),
    ('ASSISTANT_DIRECTOR','ASSISTANT_DIRECTOR'),
]

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
    def __init__(self,*args,**kwargs):
        no_admin=kwargs.pop('no_admin',False)
        no_asst=kwargs.pop('no_asst',False)
        no_delete=kwargs.pop('no_delete',False)
        super(userForm,self).__init__(*args,**kwargs)
        if no_admin:
            self.fields['userType'].choices=USER_B
        elif no_asst:
            self.fields['userType'].choices=USER_A
        elif no_delete:
            self.fields.pop('userType')
        else:
            self.fields['userType'].choices=USERTYPE


class itemsForm(forms.ModelForm):
    class Meta:
        model= itemsDB
        fields = ['item_name','item_unit','item_quantity']
        widgets = {
            'item_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Round Rags',
                    'required' : True
                    }
            ),
            'item_unit': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: pcs',
                    'required' : True
                    }
            ), 
            'item_quantity': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: 5',
                    'required' : True
                    }
            ), 
         }

class janitorForm(forms.ModelForm):
    class Meta:
        model = janitorDB
        fields = ['up_name','up_code']
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
            # 'up_status': forms.Select(
            #     attrs={
            #         'class': 'form-control',
            #         }
            # ), 
         }

class mainteForm(forms.ModelForm):
    class Meta:
        model = mainteDB
        fields = ['mp_name']
        widgets = {
            'mp_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ex: Juan Dela Cruz'
                    }
            )
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
        fields = ['req_name', 'passengers','destination', 'purpose','date','email']
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
            'email': forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'type':'email',
                        'placeholder': 'Enter Email'
                        }
                ),
        }

class clientrepairForm(forms.ModelForm):
    class Meta:
        model = clientrepairDB
        fields = '__all__'
        widgets ={
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required' : True
                    }
            ), 
            'department': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required' : True
                    }
            ), 
            'position': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required' : True
                    }
            ), 
            'prop_type': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required' : True
                    }
            ), 
            'brand': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required' : True
                    }
            ), 
            'serial': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required' : True
                    }
            ), 
            'prop_no': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required' : True
                    }
            ), 
            'acq_date': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'type':'date',
                    'required' : True
                    }
            ),
            'acq_cost': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required' : True
                    }
            ),
            'defect': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'State your Reason',
                    'required' : True
                    }
            ), 
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'email',
                    'placeholder': 'Enter Email',
                    'required' : True
                    }
            ),
        }