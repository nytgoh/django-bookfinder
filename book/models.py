from django.db import models

# Represents and contains the details of a singular book
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    avg_rating = models.IntegerField()
    rating_count = models.IntegerField()