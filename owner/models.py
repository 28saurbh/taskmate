from django.db import models
from django.forms import forms

class InfomationModel(models.Model):
    name = models.CharField(max_length=20,  blank=False)
    working = models.CharField(max_length=50,  blank=False)
    about = models.CharField(max_length=250)
    skilldes = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    

class SkillModel(models.Model):
    SkName = models.CharField(max_length=20)
    percent = models.IntegerField(blank=True)

    def __str__(self):
        return self.SkName


class PictureModel(models.Model):
    profile_picture = models.ImageField(upload_to ='images')
    about_picture = models.ImageField(upload_to= 'images')
    
