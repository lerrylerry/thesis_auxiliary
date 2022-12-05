from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USERTYPE = [
        ('ADMIN','ADMIN'),
        ('UTILITY_PERSONNEL','UTILITY_PERSONNEL'),
        ('RERAIR_MAN','REPAIR_MAN'),
        ('ASSISTANT_DIRECTOR','ASSISTANT_DIRECTOR'),
    ]

    # first column => database | second column => html forms

    userType = models.CharField(max_length=100, choices=USERTYPE, verbose_name='userType')

class itemsDB(models.Model):
    ITEMS = [
        ('Round Rags' , 'Round Rags'),
        ('Soft Broom' , 'Soft Broom'),
        ('Stick Broom' , 'Stick Broom'),
        ('Toilet Paper' , 'Toilet Paper'),
        ('Garbage Bag' , 'Garbage Bag')
    ]
    item_name = models.CharField(max_length=25, choices=ITEMS, null=True, blank=True)
    item_unit = models.CharField(max_length=25, null=True, blank=True)
    item_quantity = models.IntegerField(null=True, blank=True)

class janitorDB(models.Model):
    UP_STATUS = [
        ('ACTIVE','ACTIVE'),
        ('INACTIVE','INACTIVE')
    ]

    up_name = models.CharField(max_length=25,null=True, blank=True)
    up_code = models.CharField(max_length=4, null=True, blank=True)
    up_status = models.CharField(max_length=100, choices=UP_STATUS, verbose_name='userType')

class vehicleDB(models.Model):
    req_name = models.CharField(max_length=25,null=True, blank=True)
    passengers = models.IntegerField(null=True, blank=True)
    destination = models.CharField(max_length=25,null=True, blank=True)
    purpose = models.CharField(max_length=25,null=True, blank=True)
    date = models.DateField(max_length=10)