# Generated by Django 3.2.9 on 2021-11-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeePortal', '0005_card'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.RemoveField(
            model_name='employeebasicinfo',
            name='gendercat',
        ),
        migrations.AlterField(
            model_name='employeebasicinfo',
            name='bloodgroup',
            field=models.CharField(choices=[('A+', 'A Positive'), ('A-', 'A Negative'), ('AB+', 'AB Positive'), ('AB-', 'AB Negative'), ('B+', 'B Positive'), ('B-', 'B Negative'), ('0-', 'O Negative'), ('O+', 'O Positive')], default='A+', max_length=20),
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
    ]