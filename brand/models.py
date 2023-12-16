from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    founded_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name
