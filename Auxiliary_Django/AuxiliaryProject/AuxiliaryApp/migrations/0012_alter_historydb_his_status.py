# Generated by Django 4.1.4 on 2022-12-08 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuxiliaryApp', '0011_historydb_his_status_alter_vehicledb_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historydb',
            name='his_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
