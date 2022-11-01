from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

class soccer(models.Model):
    name = models.CharField(max_length=10)
    team = models.CharField(max_length=10)
    backnumber = models.CharField(max_length = 10)
    coach = models.CharField(max_length = 10)
    salary = models.CharField(max_length = 10)
    incentive = models.CharField(max_length = 10)