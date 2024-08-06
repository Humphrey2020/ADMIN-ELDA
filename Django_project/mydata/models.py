from django.db import models

class Product(models.Model):
      
       first_name=models.CharField(max_length =25)
       last_name=models.CharField(max_length=20)
       email=models.EmailField() 
       password=models.CharField( max_length=6)


class Profile(models.Model):
      
       username=models.CharField(max_length =25)
       #fname=models.CharField(max_length=20)
       #lname=models.CharField(max_length=20)
       email=models.EmailField()
       pass1=models.CharField( max_length=8)
       #pass2=models.CharField(max_length=8)
