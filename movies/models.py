from datetime import datetime

from django.db import models


# Create your models here.
class Movie(models.Model):
    RANKING_CHOICES = (('1', 'Terrible'),
                       ('2', 'Bad'),
                       ('3', 'Average'),
                       ('4', 'Good'),
                       ('5', 'Excellent'))

    name = models.CharField(max_length=200, unique=True)
    ranking = models.CharField(choices=RANKING_CHOICES,
                               max_length=3,
                               null=True,
                               blank=True)
    release_date = models.DateField(default=datetime.now())
