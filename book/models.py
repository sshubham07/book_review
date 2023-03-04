from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    fiction=models.BooleanField(default=False)
    non_fiction=models.BooleanField(default=False)
    fantasy=models.BooleanField(default=False)
    thriller=models.BooleanField(default=False)
    science_fiction=models.BooleanField(default=False)
    horror=models.BooleanField(default=False)
    photo=models.ImageField(upload_to='images')
    about=models.TextField()

class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    book =models.ForeignKey(Book, on_delete=models.CASCADE,null=True)
    comment=models.CharField(max_length=200)
    date=models.DateField(default=timezone.now)
    rating =models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
