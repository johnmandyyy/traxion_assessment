"""
Definition of models.
"""

from django.db import models


class Cities(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField(default = None, null = True)
    longitude = models.FloatField(default = None, null = True)

    def __str__(self):
        return self.name
