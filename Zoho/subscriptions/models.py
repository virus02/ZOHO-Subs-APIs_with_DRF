from django.db import models
from helpers.fields import JSONField

# Create your models here.
class Subs_info(models.Model):
    name = models.CharField(max_length=100)
    subsId = models.IntegerField()
    plan_code = models.CharField(max_length=100)
    productID = models.IntegerField()
    inputjson = JSONField(default=dict)

    def __str__(self):
        return self.name +'/'+ str(self.subsId)