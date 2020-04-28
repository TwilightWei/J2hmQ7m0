from django.db import models

# Create your models here.
class Record(models.Model):
    keyword_number = models.IntegerField()
    crwal_time = models.DateTimeField()