from django.db import models
from django.forms import forms


class ContactModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    contact_des = models.CharField(max_length=250)

            
               
    def __str__(self):
        return self.name
    
