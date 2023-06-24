from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=30)
    emailid = models.EmailField(max_length=30, default="")
    password = models.CharField(max_length=30)
    education = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    countryCode= models.CharField(max_length=100)
    mobile = models.CharField(max_length=30)


    def __str__(self):
       return self.username
