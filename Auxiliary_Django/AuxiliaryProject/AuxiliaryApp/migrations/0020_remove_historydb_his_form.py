# Generated by Django 4.0.1 on 2022-12-18 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuxiliaryApp', '0019_itemsdb_itemsname_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historydb',
            name='his_form',
        ),
    ]
