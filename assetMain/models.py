# asset_management/models.py
from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=50)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Asset(models.Model):
    name = models.CharField(max_length=50)
    condition = models.CharField(max_length=200)

class AssetMsg(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkOut = models.DateTimeField()
    checkIn = models.DateTimeField(null=True, blank=True)

