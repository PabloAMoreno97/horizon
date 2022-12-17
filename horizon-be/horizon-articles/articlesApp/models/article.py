from django.db import models


class Article (models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Name', max_length=50)
    description = models.CharField('Descripton', max_length=500)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    image = models.CharField('Image', max_length=1000)
