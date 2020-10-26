from django.db import models

# Create your models here.


class qrdata(models.Model):
    codename=models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
