from django.db import models


class Art(models.Model):
    ip = models.CharField(max_length=200)
    port = models.CharField(max_length=200)


class Bigtext(models.Model):
    title = models.CharField(max_length=200)
    data = models.TextField(blank=True)


class Server(models.Model):
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    comment = models.ForeignKey(Bigtext, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    os = models.CharField(max_length=200)




