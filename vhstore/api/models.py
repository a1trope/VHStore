from django.db import models
from datetime import date


class Cassette(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    released = models.DateField(default=date.today)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"\"{self.title}\" - {self.director} ({self.released.year})"
