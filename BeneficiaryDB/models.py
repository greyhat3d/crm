import email
from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.

class Beneficiary(models.Model):
    firstname = models.CharField( max_length=50,null=False)
    lastname = models.CharField( max_length=50,null=False) 
    srname = models.CharField( max_length=50,null=False)   
    gender = models.CharField( max_length=50,null=False) 
    disability = models.CharField( max_length=50,null=False) 
    education = models.CharField( max_length=50,null=False)
    phone = models.IntegerField(null=False)  
    email = models.CharField( max_length=50,null=False, unique=True)
    county = models.CharField( max_length=50,null=False) 
    location = models.CharField( max_length=50,null=False) 
    dob = models.DateField()
    dor = models.DateField()
    
    class Meta:
        verbose_name_plural = "Beneficiaries"

    def __str__(self) -> str:
        return self.firstname
