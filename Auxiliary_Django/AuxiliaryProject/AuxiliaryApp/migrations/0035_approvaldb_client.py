# Generated by Django 4.1.3 on 2022-12-29 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AuxiliaryApp', '0034_approvaldb_remove_adminrepairdb_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='approvaldb',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AuxiliaryApp.clientrepairdb'),
        ),
    ]
