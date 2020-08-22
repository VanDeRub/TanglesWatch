from django.db import models


class Milestone(models.Model):
    index = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=81)
    timestamp = models.CharField(max_length=80)
