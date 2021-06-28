from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.



class Check(models.Model):
    DONE = 'done'
    UNDONE = 'undone'
    flag = models.CharField(max_length=50,blank=True,null=True)


class Training(models.Model):
    image = models.ImageField(upload_to = 'input/')
    disease = models.CharField(max_length=100,blank=True,null=True)