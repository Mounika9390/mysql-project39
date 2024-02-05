from django.db import models

# Create your models here.
class Company(models.Model):
    cname=models.CharField(max_length=100)
    cmanager=models.CharField(max_length=100)

class Employee(models.Model):
    ename=models.CharField(max_length=100)
    cname=models.ForeignKey(Company,on_delete=models.CASCADE)