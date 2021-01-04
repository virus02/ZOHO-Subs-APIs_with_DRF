from django.db import models
from helpers.fields import JSONField

# Create your models here.
class Plan_info(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    plan_code = models.CharField(max_length=100)
    inputjson = JSONField(default=dict)

    def __str__(self):
        return self.name +'/'+ self.plan_code