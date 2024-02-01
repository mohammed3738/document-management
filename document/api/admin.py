from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(TaxFirm)
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(OwnerDetails)
admin.site.register(CustomUser)
admin.site.register(BankDetails)
admin.site.register(Gst)
admin.site.register(SalesInvoice)
admin.site.register(CreditNote)
admin.site.register(PurchaseInvoice)
admin.site.register(DebitNote)
admin.site.register(DebitProduct)
admin.site.register(ProductDetails)
admin.site.register(ProductSales)
admin.site.register(FinancialYear)
admin.site.register(Financial2Year)
admin.site.register(YourModel)
admin.site.register(ComputationFileModel)
admin.site.register(AcknowledgementFileModel)