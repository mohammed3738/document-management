from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
# class NoteSerializer(ModelSerializer):
#     class Meta:
#         model=["__all__"]



class TaxFirmSerializer(serializers.ModelSerializer):
    logo = serializers.FileField(required=False)  # Assuming logo is a FileField in your model

    class Meta:
        model = TaxFirm
        fields = ['tax_firm', 'date_of_incorporation', 'contact_person', 'entity_type', 'pan', 'gst', 'username', 'password', 'logo']

    def create(self, validated_data):
        logo = validated_data.pop('logo', None)
        tax_firm = TaxFirm.objects.create(logo=logo, **validated_data)
        return tax_firm

class CompanySerializer(ModelSerializer):
    class Meta:
        model=Company
        fields=['id','company','date_of_incorporation','contact_person','entity_type']


class UserSerializer(ModelSerializer):
    class Meta:
        model=CustomUser
        fields = ['id','username', 'contact_number', 'email','password']


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
        fields = ['id','ua_number','ua_login','ua_password','remarks','filling_freq','attachment']

class TanSerializer(ModelSerializer):

    class Meta:
        model = Tan
        fields = ['id','tan_number','tan_login','tan_password','remarks','filling_freq','attachment']

class PtrcSerializer(ModelSerializer):
    class Meta:
        model = Ptrc
        fields = ['id','ptrc_number','ptrc_login','ptrc_password','remarks','filling_freq','attachment']


class PtecSerializer(ModelSerializer):
    class Meta:
        model = Ptec
        fields = ['id','ptec_number','ptec_login','ptec_password','remarks','filling_freq','attachment']


class PanSerializer(ModelSerializer):
    class Meta:
        model = Pan
        fields = ['id','pan_number','pan_login','pan_password','remarks','filling_freq','attachment']


class MsmeSerializer(ModelSerializer):
    class Meta:
        model = Msme
        fields = ['id','msme_number','msme_login','msme_password','remarks','filling_freq','attachment']

class GstSerializer(ModelSerializer):
    class Meta:
        model = Gst
        fields = ['id','gst_number','gst_login','gst_password','remarks','filling_freq','attachment']


# class SalesInvoiceSerializer(ModelSerializer):
#     class Meta:
#         model=SalesInvoice
#         fields = ['id','party_name','month','booking_date','is_reverse','invoice_no','invoice_date','amount','cgst','gst_per','sgst','tds','tcs','in_amount','attach_invoice','attach_eway']


class ProductSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSales
        fields = ['id', 'hsn', 'product_name', 'unit_of_measure', 'unit', 'rate', 'gst_per', 'taxable_amount', 'cgst', 'sgst', 'igst']

class Branch2(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['branch']

class SalesInvoiceSerializer(serializers.ModelSerializer):
    # total_invoice = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = SalesInvoice
        fields = ['id', 'month', 'gst_no', 'party_name','total_tax_amount','total_gst', 'invoice_date', 'invoice_no', 'invoice_type', 'total_invoice', 'tcs', 'tds', 'amount_receivable', 'attach_invoice', 'attach_eway']

class SalesCompanySerializer(serializers.ModelSerializer):
    # total_invoice = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    branch_details = Branch2(source='branch', read_only=True)  # Nested field to get branch details

    class Meta:
        model = SalesInvoice
        fields = ['branch','branch_details','id', 'month', 'gst_no', 'party_name','total_tax_amount','total_gst', 'invoice_date', 'invoice_no', 'invoice_type', 'total_invoice', 'tcs', 'tds', 'amount_receivable', 'attach_invoice', 'attach_eway']


# class CreditNoteSerializer(ModelSerializer):
#     class Meta:
#         model=CreditNote
#         fields = ['id','month','gst_no','party_name','invoice_date','invoice_no','invoice_type','hsn','description','unit_of_measure','unit','rate','gst_per','taxable_amount','cgst','sgst','igst','total_invoice','tcs','tds','amount_receivable','attach_invoice','attach_eway']




class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = ['id', 'hsn', 'product_name', 'unit_of_measure', 'unit', 'rate', 'gst_per', 'taxable_amount', 'cgst', 'sgst', 'igst']


class PurchaseInvoiceSerializer(serializers.ModelSerializer):
    # total_invoice = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = PurchaseInvoice
        fields = ['id', 'month', 'gst_no', 'party_name','total_tax_amount','total_gst', 'invoice_date', 'invoice_no', 'invoice_type', 'total_invoice', 'tcs', 'tds', 'amount_receivable', 'attach_invoice', 'attach_eway']

class PurchaseCompanySerializer(serializers.ModelSerializer):
    # total_invoice = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    branch_details = Branch2(source='branch', read_only=True)  # Nested field to get branch details

    class Meta:
        model = PurchaseInvoice
        fields = ['branch','branch_details','id', 'month', 'gst_no', 'party_name','total_tax_amount','total_gst', 'invoice_date', 'invoice_no', 'invoice_type', 'total_invoice', 'tcs', 'tds', 'amount_receivable', 'attach_invoice', 'attach_eway']

        
class CreditNoteSerializer(ModelSerializer):
    class Meta:
        model=CreditNote
        fields = ['id', 'month', 'gst_no', 'party_name', 'invoice_date', 'invoice_no', 'invoice_type', 'total_invoice', 'tcs', 'tds', 'amount_receivable', 'attach_invoice', 'attach_eway']

class CreditProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditProduct
        fields = ['id', 'hsn', 'product_name', 'unit_of_measure', 'unit', 'rate', 'gst_per', 'taxable_amount', 'cgst', 'sgst', 'igst']

class DebitNoteSerializer(ModelSerializer):
    class Meta:
        model=DebitNote
        fields = ['id', 'month', 'gst_no', 'party_name', 'invoice_date', 'invoice_no', 'invoice_type', 'total_invoice', 'tcs', 'tds', 'amount_receivable', 'attach_invoice', 'attach_eway']

class DebitProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebitProduct
        fields = ['id', 'hsn', 'product_name', 'unit_of_measure', 'unit', 'rate', 'gst_per', 'taxable_amount', 'cgst', 'sgst', 'igst']



class BankStatementSerializer(ModelSerializer):
    class Meta:
        model = BankStatement
        fields = ['id','month', 'year','bank_name','amount', 'attachment']  


class InterestCertificateSerializer(ModelSerializer):
    class Meta:
        model = InterestCertificate
        fields = ['id','month', 'year','bank_name','amount', 'attachment']

class AssetsPurchasedSerializer(ModelSerializer):
    class Meta:
        model = AssetsPurchasedBill
        fields = ['id','month', 'year','bank_name','amount', 'attachment']

class LoanVoucherSerializer(ModelSerializer):
    class Meta:
        model = LoanVoucher
        fields = ['id','month', 'year','bank_name','amount', 'attachment']


class TdsCertificateSerializer(ModelSerializer):
    class Meta:
        model = TdsCertificate
        fields = ['id','month', 'year','amount' ,'attachment']


class As26Serializer(ModelSerializer):
    class Meta:
        model = As26
        fields = ['id','month', 'year', 'attachment']


class InvestmentSerializer(ModelSerializer):
    class Meta:
        model = InvestmentStatement
        fields = ['id','month', 'year','amount' 'attachment', 'type']      

class TaxReturnSerializer(ModelSerializer):
    class Meta:
        model = IncomeTaxReturn
        fields = ['id','financial_year','return_type','attachment']    
           
class ComputationFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputationFile
        fields = ('id', 'file')

class AcknowledgementFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcknowledgementFile
        fields = ('id', 'file')

class FinancialYearSerializer(serializers.ModelSerializer):
    computation = ComputationFileSerializer(many=True, read_only=True)
    acknowledgement = AcknowledgementFileSerializer(many=True, read_only=True)

    class Meta:
        model = FinancialYear
        fields = ('id', 'company', 'return_type', 'from_date', 'to_date', 'month',
                  'frequency', 'computation', 'client_review', 'remark', 'acknowledgement')   
        
class Financial2YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financial2Year
        fields = ['id','computation', 'acknowledgement']

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


# testing

class ComputationFileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputationFileModel
        fields = ['file']

class AcknowledgementFileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcknowledgementFileModel
        fields = ['file']

class YourModelSerializer(serializers.ModelSerializer):
    computation = ComputationFileModelSerializer(many=True, read_only=True)
    acknowledgement = AcknowledgementFileModelSerializer(many=True, read_only=True)

    class Meta:
        model = YourModel
        fields = ['id','return_type','from_date','to_date','month','frequency','client_review','remark','computation', 'acknowledgement']
