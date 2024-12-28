from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    cost = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="product", default="default.png", null=True, blank=True)

