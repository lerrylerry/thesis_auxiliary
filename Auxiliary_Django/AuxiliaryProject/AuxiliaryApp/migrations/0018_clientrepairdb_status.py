# Generated by Django 4.0.1 on 2022-12-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuxiliaryApp', '0017_clientrepairdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientrepairdb',
            name='status',
            field=models.CharField(default='PENDING', max_length=8),
        ),
    ]
