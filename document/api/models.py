from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

filing =[
    ('monthly','Monthly'),
    ('half-year','Half-yearly'),
    ('quarterly','Quarterly'),
    ('yearly','Yearly'),
]

class Company(models.Model):
    entities = [
        ('proprietorship', 'Proprietorship'),
        ('partnership', 'Partnership'),
        ('private_ltd', 'Private Ltd'),
        ('public_ltd', 'Public Ltd'),
        ('huf', 'HUF'),
        ('llp', 'LLP'),
        ('llc', 'LLC'),
        ('aop', 'AOP'),
        ('trust', 'Trust'),
    ]


    company = models.CharField(max_length=122)
    date_of_incorporation = models.DateField()
    contact_person = models.CharField(max_length=122)
    entity_type = models.CharField(max_length=100, choices=entities)
    file_no = models.CharField(max_length=100, unique=True)


    # def save(self):
    #     if not self.file_no and self.pk is None:
    #         last_invoice = Company.objects.all().order_by("-pk").first()
    #         last_pk = 0
    #         if last_invoice:
    #             last_pk = last_invoice.pk
        
    #         self.file_no = "SA-" + str(last_pk+1).zfill(3)

    #     super(Company, self).save()


    def __str__(self):
        return self.company + "-" 
    
# + self.file_no


class CustomUser(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,null=True, blank=True)
    contact_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.username
    

class Branch(models.Model):
    # b_entities = [
    #     ('pan', 'PAN'),
    #     ('tan', 'TAN'),
    #     ('msme', 'MSME'), 
    # ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    branch = models.CharField(max_length=122)
    # branch_entity = models.CharField(max_length=100, choices=b_entities)

    def __str__(self):
        return self.branch
    

class OwnerDetails(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    name= models.CharField(max_length=50)
    share = models.CharField(max_length=255)
    pan = models.CharField(max_length=255)
    aadhar = models.CharField(max_length=255)
    mobile =models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name
    

class BankDetails(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=50)
    account_no = models.CharField(max_length=255)
    ifsc = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50)
    branch = models.CharField( max_length=255)
    attachment = models.FileField()


    def __str__(self):
        return self.name
    

class UdyamAadhar(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    ua_number = models.CharField(max_length=255)
    ua_login = models.CharField(max_length=255)
    ua_password = models.CharField(max_length=100)
    remarks = models.CharField(max_length=500)
    filling_freq = models.CharField(max_length=100, choices = filing)
    attachment = models.FileField()


    def __str__(self):
        return self.ua_number
    


class Tan(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    tan_number = models.CharField(max_length=255)
    tan_login = models.CharField(max_length=255)
    tan_password = models.CharField(max_length=100)
    remarks = models.CharField(max_length=500)
    filling_freq = models.CharField(max_length=100, choices = filing)
    attachment = models.FileField(null=True,blank=True)


    def __str__(self):
        return self.tan_number