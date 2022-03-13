from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Udalost(models.Model):
    title_en = models.CharField(max_length= 100)
    title_cz = models.CharField(max_length= 100)
    desc_en = models.TextField()
    desc_en = models.TextField()
    date_start = models.DateField()
    date_end = models.DateField()
    author = models.ManyToManyField(Person)
