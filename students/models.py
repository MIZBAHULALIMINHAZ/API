from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    image = CloudinaryField('image')
    rating = models.FloatField(
        default=0.0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )

    def __str__(self):
        return self.name