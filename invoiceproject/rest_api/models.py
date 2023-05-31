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

class Items(models.Model):
    desc=models.TextField()
    rate=models.DecimalField(max_digits=200,decimal_places=2)
    quantity=models.IntegerField()

class InvoiceModel(models.Model):
    client_name=models.CharField(max_length=100)
    date=models.DateField()
    items=models.ForeignKey(Items,on_delete=models.CASCADE,related_name="items")
