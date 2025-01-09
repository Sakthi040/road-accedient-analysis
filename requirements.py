from django.db import models

class Accident(models.Model):
    accident_id = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=255)
    weather_conditions = models.CharField(max_length=100)
    time_of_day = models.TimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.accident_id
