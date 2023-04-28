from django.db import models
class Picture(models.Model):
    npl = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)
    timestamp = models.CharField(max_length=20)
    speed = models.FloatField()
    fullimg = models.TextField(max_length=999_999_999_999_999, null=True, blank=True)
    lp = models.TextField(max_length=999_999_999_999_999)
    aux = models.TextField(max_length=999_999_999_999_999, null=True, blank=True)
    small = models.TextField(max_length=999_999_999_999_999)
    camera = models.CharField(max_length=25)
