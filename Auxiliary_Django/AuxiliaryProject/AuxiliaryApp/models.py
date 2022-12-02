from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # username = models.CharField(max_length=100, verbose_name="username")
    # password = models.CharField(max_length=100, verbose_name="password")

    USERTYPE = [
        ('ADMIN','ADMIN'),
        ('UTILITY_PERSONNEL','UTILITY_PERSONNEL'),
        ('RERAIR_MAN','REPAIR_MAN'),
        ('ASSISTANT_DIRECTOR','ASSISTANT_DIRECTOR'),
    ]

    # first column => database | second column => html forms

    userType = models.CharField(max_length=100, choices=USERTYPE, verbose_name='userType')

class itemsDB(models.Model):
    item_name = models.CharField(max_length=25, null=True, blank=True)
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
