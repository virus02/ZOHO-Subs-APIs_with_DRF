from django.db import models
from helpers.fields import JSONField

# Create your models here.
class Customer_info(models.Model):
    display_name = models.CharField(max_length=100)
    customerID = models.IntegerField()
    email = models.EmailField()
    company_name = models.CharField(max_length=100)
    inputjson = JSONField(default=dict)

    def __str__(self):
        return self.display_name