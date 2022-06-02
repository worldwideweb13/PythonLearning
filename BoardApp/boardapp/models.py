from distutils.command.upload import upload
from django.db import models

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    autor = models.CharField(max_length=100)
    images = models.ImageField(upload_to='')
    good = models.IntegerField()
    read = models.IntegerField()
    readtext = models.CharField(max_length=200)