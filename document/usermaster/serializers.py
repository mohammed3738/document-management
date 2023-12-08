from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers



class VendorSerializer(ModelSerializer):
    class Meta:
        model=ClientVendor
        fields=['id','name','pan']

class VBranchSerializer(ModelSerializer):
    class Meta:
        model=VendorBranch
        fields=['id','name','gst','address']

    