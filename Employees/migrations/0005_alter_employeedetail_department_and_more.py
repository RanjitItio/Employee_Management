# Generated by Django 5.0.3 on 2024-03-15 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0004_alter_employeedetail_emp_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetail',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Employees.department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='employeedetail',
            name='email',
            field=models.CharField(blank=True, max_length=225, null=True, unique=True, verbose_name='Email ID'),
        ),
        migrations.AlterField(
            model_name='employeedetail',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='employeedetail',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='employeedetail',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='employeedetail',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True, verbose_name='Mobile Number'),
        ),
    ]