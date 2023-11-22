from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
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
    is_reverse = models.BooleanField(null=True,blank=True)
    booking_date = models.DateField(auto_now_add=True,null=True,blank=True)
    month = models.DateField(null=True, blank=True)
    invoice_no = models.CharField(max_length=255,null=True, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    gst_per=models.IntegerField(null=True,blank=True)
    cgst = models.IntegerField(null=True, blank=True)
    sgst = models.IntegerField(null=True, blank=True)
    tds = models.IntegerField(null=True, blank=True)
    tcs = models.IntegerField(null=True, blank=True)
    in_amount = models.IntegerField(null=True, blank=True)
    attach_invoice = models.FileField()
    attach_eway = models.FileField()


    def __str__(self):
        return f"Credit Note {self.id} - {self.invoice_no}" if self.invoice_no else f"Credit Note {self.id} - No Invoice Number"
    


class CreditNote(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True, blank=True)
    sales_in = models.ForeignKey(SalesInvoice,on_delete=models.CASCADE,null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)  
    month = models.DateField()
    party_name = models.CharField(max_length=250)
    invoice_no = models.CharField(max_length=255)
    invoice_date = models.DateField()
    amount = models.IntegerField(null=True, blank=True)
    gst_per=models.IntegerField(null=True,blank=True)
    cgst = models.IntegerField(null=True, blank=True)
    sgst = models.IntegerField(null=True, blank=True)
    tds = models.IntegerField(null=True, blank=True)
    tcs = models.IntegerField(null=True, blank=True)
    cr_amount = models.IntegerField(null=True, blank=True)
    attach_invoice = models.FileField()
    attach_eway = models.FileField()    

    
    def __str__(self):
        return f"Credit Note {self.id} - {self.invoice_no}" if self.invoice_no else f"Credit Note {self.id} - No Invoice Number"



class PurchaseInvoice(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True, blank=True)  
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)  
    party_name = models.CharField(max_length=250)
    booking_date = models.DateField(auto_now_add=True, null=True,blank=True)
    is_reverse = models.BooleanField(null=True,blank=True)
    month = models.DateField(null=True, blank=True)
    invoice_no = models.CharField(max_length=255,null=True, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    gst_per=models.IntegerField(null=True, blank=True)
    cgst = models.IntegerField(null=True, blank=True)
    sgst = models.IntegerField(null=True, blank=True)
    tds = models.IntegerField(null=True, blank=True)
    tcs = models.IntegerField(null=True, blank=True)
    in_amount = models.IntegerField(null=True, blank=True)
    attach_invoice = models.FileField()
    attach_eway = models.FileField()


    def __str__(self):
        return f"Purchase Invoice {self.id} - {self.invoice_no}" if self.invoice_no else f"Purchase Invoice {self.id} - No Invoice Number"
    


class DebitNote(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True, blank=True)
    purchase_in = models.ForeignKey(PurchaseInvoice,on_delete=models.CASCADE,null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)  
    month = models.DateField()
    party_name = models.CharField(max_length=250)
    invoice_no = models.CharField(max_length=255)
    invoice_date = models.DateField()
    amount = models.IntegerField(null=True, blank=True)
    gst_per=models.IntegerField(null=True,blank=True)
    cgst = models.IntegerField(null=True, blank=True)
    sgst = models.IntegerField(null=True, blank=True)
    tds = models.IntegerField(null=True, blank=True)
    tcs = models.IntegerField(null=True, blank=True)
    cr_amount = models.IntegerField(null=True, blank=True)
    attach_invoice = models.FileField()
    attach_eway = models.FileField()    

    
    def __str__(self):
        return f"Debit Note {self.id} - {self.invoice_no}" if self.invoice_no else f"Debit Note {self.id} - No Invoice Number"

month = [
        ('janauary','Janauary'),
		('february','February'),
		('march','March'),
		('april','April'),
		('may','May'),
		('june','June'),
		('july','July'),
		('august','August'),
		('september','September'),
		('october','October'),
		('november','November'),
		('december','December')		]


def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)  

class BankStatement(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)  
    month = models.CharField(max_length=50,choices=month)
    year = models.IntegerField(('year'), validators=[MinValueValidator(2018), max_value_current_year])   
    attachment = models.FileField()

    def __str__(self):
        return self.month.strftime("%B")
    

class InterestCertificate(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)  
    month = models.CharField(max_length=50,choices=month)
    year = models.IntegerField(('year'), validators=[MinValueValidator(2018), max_value_current_year])
    attachment = models.FileField()

    def __str__(self):
        return self.month.strftime("%B")
    
class AssetsPurchasedBill(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)  
    month = models.CharField(max_length=50,choices=month)
    year = models.IntegerField(('year'), validators=[MinValueValidator(2018), max_value_current_year])
    attachment = models.FileField()

    def __str__(self):
        return self.month.strftime("%B")
    


class LoanVoucher(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)  
    month = models.CharField(max_length=50,choices=month)
    year = models.IntegerField(('year'), validators=[MinValueValidator(2018), max_value_current_year])
    attachment = models.FileField()

    def __str__(self):
        return self.month.strftime("%B")
    

class TdsCertificate(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)  
    month = models.CharField(max_length=50,choices=month)
    year = models.IntegerField(('year'), validators=[MinValueValidator(2018), max_value_current_year])
    attachment = models.FileField()

    def __str__(self):
        return self.month.strftime("%B")


class As26(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)  
    month = models.CharField(max_length=50,choices=month)
    year = models.IntegerField(('year'), validators=[MinValueValidator(2018), max_value_current_year])
    attachment = models.FileField()

    def __str__(self):
        return self.month.strftime("%B")





types =[
    ('mutual-fund','Mutual-Fund'),
    ('equity','Equity'),
    ('fd','Fd'),
    ('others','Others'),
]



class InvestmentStatement(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)  
    month = models.CharField(max_length=50,choices=month)
    year = models.IntegerField(('year'), validators=[MinValueValidator(2018), max_value_current_year])
    type=models.CharField(max_length=100, choices=types)
    attachment = models.FileField()

    def __str__(self):
        return self.month.strftime("%B")
    
def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]



return_types=[
    ('computation-of-income','Computation-Of-Income'),
    ('financials','Financials'),
    ('income-tax-form','Income-Tax-Form'),
    ('income-tax-return','Income-Tax-Return'),
    ('tax-audit','Tax-Audit'),
    ('cma','CMA'),
    ('auditors-report','Auditors-Report'),
]

class IncomeTaxReturn(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)  
    financial_year = models.DateField()
    return_type = models.CharField(max_length=100, choices=return_types)
    attachment = models.FileField()


    def __str__(self):
        return self.return_type
    
