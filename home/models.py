from django.db import models
from django import forms

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

DOZ_CHOICES= [
    ('1doz', '1 Dozen'),
    ('2doz', '2 Dozen'),
    ('3doz', '3 Dozen'),
    ('4doz', '4 Dozen'),
    ('5doz', '5 Dozen (Peti)')
    ]
 
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
