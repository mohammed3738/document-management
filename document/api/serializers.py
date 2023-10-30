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
        fields = ['username', 'contact_number', 'email','password']


class BranchSerializer(ModelSerializer):
    class Meta:
        model=Branch
        fields = ['id','branch','address']


class OwnerSerializer(ModelSerializer):
    class Meta:
        model = OwnerDetails
        fields = ['id','name','share','pan','aadhar','mobile','email']



class BankSerializer(ModelSerializer):
    class Meta:
        model = BankDetails
        fields = ['id','name','account_no','ifsc','account_type','branch','attachment']


class AadharSerializer(ModelSerializer):
    class Meta:
        model = UdyamAadhar
        fields = ['ua_number','ua_login','ua_password','remarks','filling_freq','attachment']

class TanSerializer(ModelSerializer):

    class Meta:
        model = Tan
        fields = ['tan_number','tan_login','tan_password','remarks','filling_freq','attachment']

class PtrcSerializer(ModelSerializer):
    class Meta:
        model = Ptrc
        fields = ['ptrc_number','ptrc_login','ptrc_password','remarks','filling_freq','attachment']


class PtecSerializer(ModelSerializer):
    class Meta:
        model = Ptec
        fields = ['ptec_number','ptec_login','ptec_password','remarks','filling_freq','attachment']

# class CompanySerializer(ModelSerializer):

#     class Meta:
#         model = Company
#         fields = ['company','date_of_incorporation','contact_person','entity_type']


# {
#   "username": "mohammed",
#   "contact_number": "20234578965",
#   "email": "baigm066@gmail.com",
#   "password1": "123456789#",
#   "password2": "123456789#"
# }