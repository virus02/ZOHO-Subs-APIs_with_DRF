from django.db import models
from helpers.fields import JSONField

# Create your models here.
class Product_info(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    productID = models.IntegerField()
    inputjson = JSONField(default=dict)

    def __str__(self):
        return self.name +'/'+ str(self.productID)