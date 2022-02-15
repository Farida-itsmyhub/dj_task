from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class Table(models.Model):
    name = models.CharField(max_length=100, blank=True)
    price = models.CharField(max_length=100)
    max_speed = models.CharField(max_length=200)
    year = models.IntegerField()
    image = models.ImageField(upload_to='posts/%Y/%m/%d/', blank=True)
    cars = PublishedManager()

    def __str__(self):
        return '{}'.format(self.name)
