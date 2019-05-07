from django.db import models
from  django.shortcuts import reverse
# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    nationality=models.CharField(max_length=40)
    primary=models.CharField(max_length=40)
    highSchool=models.CharField(max_length=40)
    email=models.EmailField()
    occupation=models.CharField(max_length=20)
    principle=models.CharField(max_length=100)
    residence=models.CharField(max_length=50)
    campus=models.CharField(max_length=30)
    course=models.CharField(max_length=20)
    hobby=models.CharField(max_length=100)
    image=models.ImageField()
    is_female=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('Emmaculate:index')