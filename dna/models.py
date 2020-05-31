from django.contrib.postgres.fields import ArrayField
from django.db import models


class Dna(models.Model):
    dna = ArrayField(models.CharField(max_length=6, blank=True))
