# Generated by Django 4.1.3 on 2023-01-03 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuxiliaryApp', '0036_approvaldb_optional'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintedb',
            name='mp_password',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='maintedb',
            name='mp_username',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]