from django.db import models


class Registration(models.Model):
    firstName=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField()
    password=models.CharField(max_length=50)
    confirmPassword=models.CharField(max_length=50)

class Login(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=50)    