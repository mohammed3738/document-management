from rest_framework.serializers import ModelSerializer
from .models import *

# class NoteSerializer(ModelSerializer):
#     class Meta:
#         model=["__all__"]



class CompanySerializer(ModelSerializer):
    class Meta:
        model=Company
        fields=['id','company','date_of_incorporation','contact_person','entity_type']


class UserSerializer(ModelSerializer):
    class Meta:
        model=CustomUser
        fields = ['username', 'contact_number', 'email','password1','password2']


# class CompanySerializer(ModelSerializer):

#     class Meta:
#         model = Company
#         fields = ['company','date_of_incorporation','contact_person','entity_type']