from django.db import models

# Create your models here.
class Customer(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    adhar=models.CharField(max_length=10)
    phone=models.CharField(max_length=10)
    accno=models.PositiveBigIntegerField()
    