from django.conf import settings
from django.db import models
from django.utils import timezone

class Pitchingdata(models.Model):

    kyusyumark=models.CharField(max_length=100)
    numberofpitch=models.IntegerField()
    balltype=models.CharField(max_length=100)
    ballspeed=models.IntegerField()
    result=models.CharField(max_length=100)
    course=models.IntegerField()
    first=models.IntegerField()
    second=models.IntegerField()
    third=models.IntegerField()
    hometeam=models.CharField(max_length=100)
    visitorteam=models.CharField(max_length=100)
    pitcher=models.CharField(max_length=100)
    batter=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    B=models.IntegerField()
    S=models.IntegerField()
    O=models.IntegerField()
    hit=models.IntegerField()
    walk=models.IntegerField()
    out=models.IntegerField()
    strikeout=models.IntegerField()
