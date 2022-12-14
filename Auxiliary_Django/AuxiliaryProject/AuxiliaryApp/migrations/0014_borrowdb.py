# Generated by Django 4.0.1 on 2022-12-14 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AuxiliaryApp', '0013_delete_borrowdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='borrowDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_req', models.JSONField(default=dict)),
                ('status', models.CharField(default='PENDING', max_length=8)),
                ('utility_personnel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AuxiliaryApp.janitordb')),
            ],
        ),
    ]
