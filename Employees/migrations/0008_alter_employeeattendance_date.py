# Generated by Django 5.0.3 on 2024-03-15 12:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0007_alter_employeeattendance_out_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeattendance',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
    ]