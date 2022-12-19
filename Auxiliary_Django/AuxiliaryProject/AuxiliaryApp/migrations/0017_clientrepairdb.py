# Generated by Django 4.0.1 on 2022-12-15 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuxiliaryApp', '0016_borrowdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientrepairDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('position', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('prop_type', models.CharField(blank=True, max_length=50, null=True)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('serial', models.CharField(blank=True, max_length=50, null=True)),
                ('prop_no', models.CharField(blank=True, max_length=50, null=True)),
                ('acq_date', models.DateField(max_length=10)),
                ('acq_cost', models.IntegerField(blank=True, null=True)),
                ('defect', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]