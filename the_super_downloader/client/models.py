from django.db import models
from django.contrib.auth.models import User

class Format(models.Model):
    name = models.CharField(max_length = 100 , null = False, blank = False)
    extensions = models.CharField(max_length=500, null = False, blank = False) #dumped JSON contains: string list with extensions Ex. (".mp4")

class Download(models.Model):

    format = models.ForeignKey(Format, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50 , null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    key = models.CharField(max_length=250, null=False, blank=False)
    miniature_key = models.CharField(max_length=250, null=True, blank=True)

    #optional
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
