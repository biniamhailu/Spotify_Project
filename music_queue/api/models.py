from django.db import models

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    member_can_pause = models.BooleanField(null=False, default=False)
    skip_votes = models.IntegerField(null=False, default=1)
    