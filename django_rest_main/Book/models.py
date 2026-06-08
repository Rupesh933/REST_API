
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self) ->str:
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)  # isbn means International Standard Book Number
    published = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title