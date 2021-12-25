from django.db import models


# Create your models here.

class Restaurants(models.Model):
    rid = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 1000)
    type = models.CharField(max_length = 500)
    description = models.CharField(max_length = 10000)
    hours = models.JSONField()

    class Meta:
        db_table = "restaurants"
