from django.db import models


class Art(models.Model):
    ip = models.CharField(max_length=200)
    port = models.CharField(max_length=200)


class Bigtext(models.Model):
    title = models.CharField(max_length=200)
    data = models.TextField(blank=True)
