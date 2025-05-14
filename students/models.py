from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    image = CloudinaryField('image')
    
    def __str__(self):
        return self.name