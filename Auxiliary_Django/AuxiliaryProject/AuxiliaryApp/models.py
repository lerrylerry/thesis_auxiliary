from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USERTYPE = [
        ('ADMIN','ADMIN'),
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
    up_name = models.CharField(max_length=25,null=True, blank=True)
    up_code = models.CharField(max_length=4, null=True, blank=True)
    up_status = models.CharField(max_length=100, verbose_name='userType', default='ACTIVE')

class mainteDB(models.Model):
    mp_name = models.CharField(max_length=25,null=True, blank=True)
    mp_status = models.CharField(max_length=100, default='ACTIVE')

class vehicleDB(models.Model):
    req_name = models.CharField(max_length=25,null=True, blank=True)
    passengers = models.IntegerField(null=True, blank=True)
    destination = models.CharField(max_length=25,null=True, blank=True)
    purpose = models.CharField(max_length=25,null=True, blank=True)
    date = models.DateField(max_length=10)
    email = models.EmailField(max_length=300, default=None)
    status = models.CharField(max_length=100, verbose_name='status', default='PENDING')

class borrowDB(models.Model):
    utility_personnel = models.ForeignKey(janitorDB, on_delete=models.CASCADE)
    items_req = models.JSONField(default=dict)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8, default="PENDING")

class historyDB(models.Model):
    his_name = models.CharField(max_length=50,null=True, blank=True)
    service = models.CharField(max_length=50,null=True, blank=True)
    his_date = models.DateTimeField(auto_now_add=True)
    his_status = models.CharField(max_length=50,null=True, blank=True)
    borrow = models.ForeignKey(borrowDB, on_delete=models.CASCADE,null=True)
    vehicle = models.ForeignKey(vehicleDB, on_delete=models.CASCADE,null=True)

class clientrepairDB(models.Model):
    name = models.CharField(max_length=50,null=True, blank=True)
    department = models.CharField(max_length=50,null=True, blank=True)
    position = models.CharField(max_length=50,null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    ##########desc of prop##########
    prop_type = models.CharField(max_length=50,null=True, blank=True)
    brand = models.CharField(max_length=50,null=True, blank=True)
    serial = models.CharField(max_length=50,null=True, blank=True)
    prop_no = models.CharField(max_length=50,null=True, blank=True)
    acq_date = models.DateField(max_length=10)
    acq_cost = models.IntegerField(null=True, blank=True)
    defect = models.CharField(max_length=500,null=True, blank=True)
    status = models.CharField(max_length=8, default="PENDING",blank=True)
    email = models.EmailField(max_length=300, default=None)

class adminrepairDB(models.Model):
    CAN_DO = [
        ('YES', 'Can be Repaired/Fabricated in-house'),
        ('NO', "Can't be Repaired/Fabricated in-house")
    ]
    fabricate = models.CharField(max_length=100, choices=CAN_DO)
    assess = models.CharField(max_length=50,null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    assigned = models.CharField(max_length=50,null=True, blank=True)
    # assigned = models.ForeignKey(janitorDB, on_delete=models.CASCADE)

    client = models.ForeignKey(clientrepairDB, on_delete=models.CASCADE)

class mainterepairDB(models.Model):
    person = models.CharField(max_length=50,null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    inspect = models.CharField(max_length=50,null=True, blank=True)
    admin = models.ForeignKey(adminrepairDB, on_delete=models.CASCADE)

class returnclientDB(models.Model):
    DECISION = [
        ('APPROVED', 'APPROVED'),
        ('DISAPPROVED', 'DISAPPROVED'),
    ]
    requisitioner = models.CharField(max_length=50,null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    mainte = models.ForeignKey(mainterepairDB, on_delete=models.CASCADE)

class suppmatDB(models.Model):
    unit = models.CharField(max_length=50,null=True, blank=True)
    quantity = models.CharField(max_length=50,null=True, blank=True)
    particulars = models.CharField(max_length=50,null=True, blank=True)
    client = models.ForeignKey(clientrepairDB, on_delete=models.CASCADE)

class approvalDB(models.Model):
    DECISION = [
        ('APPROVED', 'APPROVED'),
        ('DISAPPROVED', 'DISAPPROVED'),
        ('RESUBMIT REQUEST', 'RESUBMIT REQUEST'),
    ]
    prove = models.CharField(max_length=100, choices=DECISION)
    head = models.CharField(max_length=50,null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(clientrepairDB, on_delete=models.CASCADE, default=1)
