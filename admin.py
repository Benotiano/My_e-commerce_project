
from __future__ import unicode_literals

from


from django.db import models


class Product(models.Model):
    name = models.CharField(max_length= 225)
    price = models.FloatField()
    stocks = models.IntegerField()
    image_url = models.CharField(max_length=2083)

from __future__ import unicode_literals

from


from django.db import models


class Product(models.Model):
    name = models.CharField(max_length= 225)
    price = models.FloatField()
    stocks = models.IntegerField()
    image_url = models.CharField(max_length=2083)
