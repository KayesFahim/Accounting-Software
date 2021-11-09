from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

# Create your models here.

class EmployeeBasicInfo(models.Model):

    Bloodgroups = (
        ('A+', 'A Positive'),
        ('A-', 'A Negative'),
        ('AB+', 'AB Positive'),
        ('AB-', 'AB Negative'),
        ('B+', 'B Positive'),
        ('B-', 'B Negative'),
        ('0-', 'O Negative'),
        ('O+', 'O Positive'),
    )

    Gender = (
        ('M', 'Male'),
        ('F-', 'Female'),
        ('N', 'None'),      
    )
    Nationality = (
        ('BN', 'Bangladesh'),
        ('PL', 'Poland'),
        ('UAE', 'Dubai'),
        ('IN','India')      
    )
    MaritalStatus = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('I', 'In a relationship'),  
        ('E', 'Engagged'),
        ('D', 'Divorced')    
    )

    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    fatherName = models.CharField(max_length=200, null=False, blank=True)
    motherName = models.CharField(max_length=200, null=False, blank=True)
    image = models.ImageField(null=True,blank=True)
    address = models.TextField(max_length=200, null=False, blank=True)
    spouseName = models.CharField(max_length=200, null=True, blank=True)
    nationaId = models.CharField(max_length=20, default='BN', choices=Nationality)
    bloodgroup = models.CharField(max_length=20, default='A+', choices=Bloodgroups)
    gender = models.CharField(max_length=20, default='N', choices=Gender)
    meritalStatus = models.CharField(max_length=20, default='S', choices=MaritalStatus)
    dateofbirth = models.DateTimeField(auto_now_add=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    sallery = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    insuranceNumber = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    tinNumber = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    id = models.AutoField(primary_key=True, editable=False)
    confirmationDate = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    lastpaidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    joindate = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    resignDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
