from django.db import models

# Create your models here.
title_choices=[
    ("MR","Mr."),
    ("MRS","Msrs."),
    ("MS","Ms.")
]

class Author(models.Model):
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=3,choices=title_choices)
    birth_date=models.DateField(blank=True,null=True )

    def __str__(self) -> str:
        return self.name
    
class Book(models.Model):
    name=models.CharField(max_length=100)
    authors=models.ManyToManyField(Author)

