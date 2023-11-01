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
    # file_no = models.CharField(max_length=100, unique=True)


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
    address = models.CharField(max_length=255)
    # branch_entity = models.CharField(max_length=100, choices=b_entities)

    def __str__(self):
        return self.branch
    

class OwnerDetails(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    name= models.CharField(max_length=50)
    share = models.IntegerField()
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
    

class Ptrc(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    ptrc_number = models.CharField(max_length=255)
    ptrc_login = models.CharField(max_length=255)
    ptrc_password = models.CharField(max_length=100)
    remarks = models.CharField(max_length=500)
    filling_freq = models.CharField(max_length=100, choices = filing)
    attachment = models.FileField()


    def __str__(self):
        return self.ptrc_number
    

class Ptec(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    ptec_number = models.CharField(max_length=255)
    ptec_login = models.CharField(max_length=255)
    ptec_password = models.CharField(max_length=100)
    remarks = models.CharField(max_length=500)
    filling_freq = models.CharField(max_length=100, choices = filing)
    attachment = models.FileField()


    def __str__(self):
        return self.ptec_number
    

class Pan(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    pan_number = models.CharField(max_length=255)
    pan_login = models.CharField(max_length=255)
    pan_password = models.CharField(max_length=100)
    remarks = models.CharField(max_length=500)
    filling_freq = models.CharField(max_length=100, choices = filing)
    attachment = models.FileField()


    def __str__(self):
        return self.pan_number
    

class Msme(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    msme_number = models.CharField(max_length=255)
    msme_login = models.CharField(max_length=255)
    msme_password = models.CharField(max_length=100)
    remarks = models.CharField(max_length=500)
    filling_freq = models.CharField(max_length=100, choices = filing)
    attachment = models.FileField()


    def __str__(self):
        return self.msme_number
    

class Gst(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True, blank=True)
    gst_number = models.CharField(max_length=255)
    gst_login = models.CharField(max_length=255)
    gst_password = models.CharField(max_length=100)
    remarks = models.CharField(max_length=500)
    filling_freq = models.CharField(max_length=100, choices = filing)
    attachment = models.FileField()

    def __str__(self):
        return self.gst_number
    

class SalesInvoice(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)  
    party_name = models.CharField(max_length=250)
    month = models.DateField(null=True, blank=True)
    invoice_no = models.CharField(max_length=255,null=True, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    amount = models.CharField(max_length=200,null=True, blank=True)
    cgst = models.CharField(max_length=255,null=True, blank=True)
    sgst = models.CharField(max_length=255,null=True, blank=True)
    tds = models.CharField(max_length=255,null=True, blank=True)
    tcs = models.CharField(max_length=255,null=True, blank=True)
    in_amount = models.CharField(max_length=255,null=True, blank=True)
    attach_invoice = models.FileField()
    attach_eway = models.FileField()


    def __str__(self):
        return self.invoice_no