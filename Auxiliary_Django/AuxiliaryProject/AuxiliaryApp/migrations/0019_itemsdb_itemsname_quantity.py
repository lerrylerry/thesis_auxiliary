# Generated by Django 4.0.1 on 2022-12-18 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuxiliaryApp', '0018_clientrepairdb_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemsdb',
            name='itemsName_Quantity',
            field=models.JSONField(default=dict),
        ),
    ]