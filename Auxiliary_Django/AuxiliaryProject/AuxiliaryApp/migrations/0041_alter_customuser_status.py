# Generated by Django 4.1.4 on 2023-01-04 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuxiliaryApp', '0040_customuser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(default='ACTIVE', max_length=100),
        ),
    ]
