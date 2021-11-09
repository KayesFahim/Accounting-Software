# Generated by Django 3.2.9 on 2021-11-09 11:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeePortal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeacademicinfo',
            name='EmployeeBasicInfo',
        ),
        migrations.RemoveField(
            model_name='employeecontactinfo',
            name='BasicInfo',
        ),
        migrations.RemoveField(
            model_name='employeejobinfo',
            name='EmployeeBasicInfo',
        ),
        migrations.RemoveField(
            model_name='employeenomineeinfo',
            name='EmployeeBasicInfo',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='employeebasicinfo',
            name='confirmationDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employeebasicinfo',
            name='insuranceNumber',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='employeebasicinfo',
            name='isPaid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employeebasicinfo',
            name='joindate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employeebasicinfo',
            name='lastpaidAt',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employeebasicinfo',
            name='paymentMethod',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employeebasicinfo',
            name='resignDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employeebasicinfo',
            name='sallery',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='employeebasicinfo',
            name='tinNumber',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.DeleteModel(
            name='EmployeeAcademicInfo',
        ),
        migrations.DeleteModel(
            name='EmployeeContactInfo',
        ),
        migrations.DeleteModel(
            name='EmployeeJobInfo',
        ),
        migrations.DeleteModel(
            name='EmployeeNomineeInfo',
        ),
    ]
