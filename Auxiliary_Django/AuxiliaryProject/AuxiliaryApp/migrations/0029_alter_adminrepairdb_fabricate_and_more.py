# Generated by Django 4.1.3 on 2022-12-20 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuxiliaryApp', '0028_adminrepairdb_mainterepairdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminrepairdb',
            name='fabricate',
            field=models.CharField(choices=[('0', 'Can be Repaired/Fabricated in-house'), ('1', "Can't be Repaired/Fabricated in-house")], max_length=100),
        ),
        migrations.AlterField(
            model_name='adminrepairdb',
            name='prove',
            field=models.CharField(choices=[('0', 'APPROVED'), ('1', 'DISAPPROVED'), ('2', 'RESUBMIT REQUEST')], max_length=100),
        ),
    ]