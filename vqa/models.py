from django.db import models

# Create your models here.

class VQA(models.Model):
    image = models.ImageField(upload_to='images/')
    text = models.CharField(max_length=200, default='')
    answer = models.CharField(max_length=200, default='')

