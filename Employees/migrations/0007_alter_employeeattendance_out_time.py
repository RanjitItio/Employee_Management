# Generated by Django 5.0.3 on 2024-03-15 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0006_employeeattendance_in_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeattendance',
            name='out_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Out Time'),
        ),
    ]
