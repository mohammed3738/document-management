from django.db import models
from api.models import Company
# Create your models here.


class ClientVendor(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    pan = models.CharField(max_length=100)

    def __str__(self):
        return self.name +"-"f"{self.id}"


class VendorBranch(models.Model):
    vendor=models.ForeignKey(ClientVendor,on_delete=models.CASCADE,null=True,blank=True)
    gst = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name +"-"f"{self.id}"



