from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Book (models.Model):
    title= models.CharField (max_length=100)
    author =models.ForeignKey(User, on_delete=models.CASCADE)
    published_date=models.DateTimeField()
    isbn=models.CharField(max_length=13, unique=True)

    def __str__(self) -> str:
        return self.title
    
