from django.db import models


class Weather(models.Model):
    temperature = models.FloatField()
    feels_like = models.FloatField()
    icon = models.CharField(max_length=255, null=True, blank=True)
    summary = models.CharField(max_length=255, null=True, blank=True)
