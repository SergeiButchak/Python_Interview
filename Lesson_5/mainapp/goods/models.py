from django.db import models

# Create your models here.


class Good(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    receipt_date = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=20)
    vendor_name = models.CharField(max_length=256, null=False, blank=False)
