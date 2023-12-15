from django.contrib import admin
from .models import *

# Register your models here.

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
admin.site.register(ProductDetails)