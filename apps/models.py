from django.db import models
class Picture(models.Model):
    npl = models.CharField()
    time = models.DateTimeField(auto_now_add=True)
    timestamp = models.CharField()
    speed = models.FloatField()
    fullimg = models.TextField(null=True, blank=True)
    lp = models.TextField()
    aux = models.TextField(null=True, blank=True)
    small = models.TextField()
    camera = models.CharField()
