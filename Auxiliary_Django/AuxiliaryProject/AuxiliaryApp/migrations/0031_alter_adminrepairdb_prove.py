# Generated by Django 4.1.3 on 2022-12-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuxiliaryApp', '0030_returnclientdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminrepairdb',
            name='prove',
            field=models.CharField(choices=[('APPROVED', 'APPROVED'), ('DISAPPROVED', 'DISAPPROVED'), ('RESUBMIT REQUEST', 'RESUBMIT REQUEST')], max_length=100),
        ),
    ]
