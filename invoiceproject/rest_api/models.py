from django.db import models


class Registration(models.Model):
    First_Name=models.CharField(max_length=200)
    Last_Name=models.CharField(max_length=200)
    Email=models.EmailField()
    Phone=models.IntegerField()
    Password=models.CharField(max_length=50)
    ConfirmPassword=models.CharField(max_length=50)