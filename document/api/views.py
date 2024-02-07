from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from .models import*
from .serializers import *
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from .forms import *
from rest_framework.parsers import MultiPartParser

from rest_framework import generics
from .serializers import YourModelSerializer

from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView











from usermaster.models import *
from usermaster.serializers import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@api_view(['GET'])
def Home(request):
    routes=[
       {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "is_student": False,
    "address": {
      "street": "123 Main Street",
      "city": "Anytown",
      "zipcode": "12345"
    },
    "hobbies": ["reading", "hiking", "photography"]
        }
    ] 
    return Response(routes)



# @api_view(['POST'])
# def create_user(request, company_id):
#     company = get_object_or_404(Company, id=company_id)

#     if request.method == "POST":
#         user_form = UserForm(request.POST)
#         if user_form.is_valid():
#             user = user_form.save(commit=False)
#             user.company = company
#             user.save()
            
#             # Extract email and username from the form data
#             user_email = user_form.cleaned_data['email']
#             username = user_form.cleaned_data['username']
#             password = user_form.cleaned_data['password1']
            
#             # Prepare email content
#             subject = "User Credentials"
#             message = f"Your login credentials:\nUsername: {username}\nPassword: {password}"
#             from_email = "mmbaig461@gmail.com"
#             recipient_list = [user_email]
            
#             # Send email
#             send_mail(subject, message, from_email, recipient_list, fail_silently=False)

#             # Serialize the user data
#             user_serializer = UserSerializer(user)

#             return Response(user_serializer.data, status=status.HTTP_201_CREATED)

#     else:
#         user_form = UserForm()


#     return Response({'user_form':user_form.data}, status=status.HTTP_200_OK)

# ////////////////////tax firm views///////////////////////
@api_view(['POST'])
def create_tax_firm(request):
    if request.method == "POST":
        firm_serializer = TaxFirmSerializer(data=request.data)

        if firm_serializer.is_valid():
            print("tax_firm_serializer",firm_serializer)
            firm_serializer.save()
            return Response({"message": "Tax Firm created successfully"}, status=status.HTTP_201_CREATED)

        return Response({"message": "Not created", "errors": firm_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def tax_firm_update(request,pk):
    tax_firm = get_object_or_404(TaxFirm, id=pk)
    tax_firm_serializer = TaxFirmSerializer(data=request.data, instance=tax_firm)
    if request.method=="POST":
        if tax_firm_serializer.is_valid():
            
           
            tax_firm_serializer.save()
            return Response({'message':'Tax Firm updated successfully!'},status=status.HTTP_200_OK)
        return Response(tax_firm_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='GET':
        # return Response(owner_serializer.initial_data,{'message':"working"})
        tax_firm_serializer_1 = TaxFirmSerializer(tax_firm)
        return Response(tax_firm_serializer_1.data)


@api_view(['DELETE'])
def tax_firm_delete(request,pk):
    tax_firm = TaxFirm.objects.get(id=pk)
    tax_firm.delete()
    return Response({"message": "Tax Firm deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def tax_firm_list(request):
    firm_list = TaxFirm.objects.all()
    serializer=TaxFirmSerializer(firm_list,many=True)
    return Response(serializer.data)


# company create view


@api_view(['POST'])
def create_company(request, id):
    tax_firm = TaxFirm.objects.filter(id=id).first()  # Use .first() to get the first matching object

    if request.method == "POST":
        company_serializer = CompanySerializer(data=request.data)

        if company_serializer.is_valid():
            # Pass tax_firm as an instance when saving the company
            company_serializer.save(tax_firm=tax_firm)
            return Response({"message": "Company created successfully"}, status=status.HTTP_201_CREATED)

        return Response({"message": "Not created", "errors": company_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def company_list(request,id):
    firm_list = TaxFirm.objects.get(id=id)
    company_lists=Company.objects.filter(tax_firm=firm_list)
    serializer=CompanySerializer(company_lists,many=True)
    print(serializer)
    return Response(serializer.data)

@api_view(['GET'])
def company_api(request, pk):
    company = Company.objects.get(id=pk)
    serializer=CompanySerializer(company)
    return Response(serializer.data)
  
@api_view(['GET'])
def company_details(request,pk):
    company = Company.objects.get(id=pk)
    owner_list = OwnerDetails.objects.filter(company=company)
    branch_list = Branch.objects.filter(company=company)
    user_list = CustomUser.objects.filter(company=company)
    bank_list = BankDetails.objects.filter(company=company)
    aadhar_list = UdyamAadhar.objects.filter(company=company)
    tan_list = Tan.objects.filter(company=company)
    ptrc_list = Ptrc.objects.filter(company=company)
    ptec_list = Ptec.objects.filter(company=company)
    pan_list = Pan.objects.filter(company=company)
    msme_list = Msme.objects.filter(company=company)
    bank_statement = BankStatement.objects.filter(company=company)
    interest_certificate = InterestCertificate.objects.filter(company=company)
    assest_purchased = AssetsPurchasedBill.objects.filter(company=company)
    loan_voucher = LoanVoucher.objects.filter(company=company)
    tds_certificate = TdsCertificate.objects.filter(company=company)
    as26 = As26.objects.filter(company=company)
    investment = InvestmentStatement.objects.filter(company=company)
    tax = IncomeTaxReturn.objects.filter(company=company)
    vendor = ClientVendor.objects.filter(company=company)
    purchase_invoice=PurchaseInvoice.objects.filter(branch__company=company)
    sales_invoice=SalesInvoice.objects.filter(branch__company=company)
    report=YourModel.objects.filter(company=company)
    # branch = purchase_invoice.branch
    
    # filter ends here
    
    owner_serializer = OwnerSerializer(owner_list,many=True)
    branch_serializer = BranchSerializer(branch_list,many=True)
    user_serializer = UserSerializer(user_list,many=True)
    bank_serializer = BankSerializer(bank_list,many=True)
    aadhar_serializer = AadharSerializer(aadhar_list,many=True)
    tan_serializer = TanSerializer(tan_list,many=True)
    ptrc_serializer = PtrcSerializer(ptrc_list,many=True)
    ptec_serializer = PtecSerializer(ptec_list,many=True)
    pan_serializer = PanSerializer(pan_list,many=True)
    msme_serializer = MsmeSerializer(msme_list,many=True)
    bank_statement_serializer = BankStatementSerializer(bank_statement,many=True)
    interest_certificate_serializer = InterestCertificateSerializer(interest_certificate,many=True)
    assest_purchased_serializer = AssetsPurchasedSerializer(assest_purchased,many=True)
    loan_voucher_serializer = LoanVoucherSerializer(loan_voucher,many=True)
    tds_certificate_serializer = TdsCertificateSerializer(tds_certificate,many=True)
    as26_serializer = As26Serializer(as26,many=True)
    investment_serializer = InvestmentSerializer(investment,many=True)
    tax_serializer = TaxReturnSerializer(tax,many=True)
    vendor_serializer = VendorSerializer(vendor,many=True)
    purchase_serializer = PurchaseCompanySerializer(purchase_invoice,many=True)
    sales_serializer = SalesCompanySerializer(sales_invoice,many=True)
    
    serialized_data = purchase_serializer.data
    report_serializer = YourModelSerializer(report,many=True)
    print("purchae:",serialized_data)
  
       

    data = {
        "owners": owner_serializer.data,
        "branches": branch_serializer.data,
        "users":user_serializer.data,
        "bank":bank_serializer.data,
        "aadhar":aadhar_serializer.data,
        "tan":tan_serializer.data,
        "ptrc":ptrc_serializer.data,
        "ptec":ptec_serializer.data,
        "pan":pan_serializer.data,
        "msme":msme_serializer.data,
        "Bank_statement":bank_statement_serializer.data,
        "interest_certificate":interest_certificate_serializer.data,
        "assest_purchased":assest_purchased_serializer.data,
        "loan_voucher":loan_voucher_serializer.data,
        "tds_certificate":tds_certificate_serializer.data,
        "as26":as26_serializer.data,
        "investment":investment_serializer.data,
        "tax":tax_serializer.data,
        "vendor":vendor_serializer.data,
        "purchase":purchase_serializer.data,
        "sales":sales_serializer.data,
        "report":report_serializer.data,
    }
    return Response(data)


@api_view(['PUT'])
def company_update(request, pk):
    company = Company.objects.get(id=pk)
    # serializer=CompanySerializer(company)

    # if request.method=="PUT":
    company_serializer = CompanySerializer(instance=company, data=request.data)
    if company_serializer.is_valid():
        company_serializer.save()
        return Response({'message':'Company updated successfully!'},status=status.HTTP_200_OK)
    return Response(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # return Response({'message':'Method not allowed'},serializer,status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def company_delete(request,pk):
    company = Company.objects.get(id=pk)
    company.delete()
    return Response({"message": "Company deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# **************************Company Views Ends****************************

# **************************User Views Start******************************

@api_view(['POST'])
def create_user(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    if request.method == "POST":
        print("post is working")
        user_serializer = UserSerializer(data=request.data)  # Use UserSerializer to validate the data
        if user_serializer.is_valid():
            print("Serializer is valid")
            user_serializer.save(company=company)  # Save the user with the associated company

            # Extract email and username from the validated data
            user_email = user_serializer.validated_data.get('email')
            username = user_serializer.validated_data.get('username')
            password = user_serializer.validated_data.get('password')

            # Prepare email content
            subject = "User Credentials"
            message = f"Your login credentials:\nUsername: {username}\nPassword: {password}"
            from_email = "mmbaig461@gmail.com"
            recipient_list = [user_email]

            # Send email
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return Response({'message':'Created User Successfully'},status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    print("Serializer is not valid")

    return Response({'message':'Error'},status=status.HTTP_400_BAD_REQUEST)


# *****************************update user views********************************


@api_view(['POST'])
def user_update(request, pk, user_pk):
    company = Company.objects.get(id=pk)
    user = CustomUser.objects.get(id=user_pk)

    if request.method=="POST":
        user_serializer = UserSerializer(instance=user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save(company=company)
            return Response({'message':'User updated successfully!'},status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


# *****************************create branch views********************************
@api_view(['POST'])
def create_branch(request, pk):
    company = get_object_or_404(Company, id=pk)

    if request.method == 'POST':
        branch_serializer = BranchSerializer(data=request.data)
        if branch_serializer.is_valid():
            branch_serializer.save(company=company)
            return Response({'message': 'Branch created successfully.'}, status=status.HTTP_201_CREATED)

    return Response(branch_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST','GET'])
def update_branch(request,pk, branch_pk):
    company = get_object_or_404(Company, id=pk)
    branch = get_object_or_404(Branch, id=branch_pk)
    branch_serializer = BranchSerializer(data=request.data, instance=branch)

    if request.method=="POST":
        if branch_serializer.is_valid():
           
            branch_serializer.save(company=company)
            return Response({'message':'Branch updated successfully!'},status=status.HTTP_200_OK)
        return Response(branch_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='GET':
        # return Response(owner_serializer.initial_data,{'message':"working"})
        branch_serializer_1 = BranchSerializer(branch)
        return Response(branch_serializer_1.data)
    # return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['DELETE'])
def delete_branch(request,pk,branch_pk):
    branch = Branch.objects.get(id=branch_pk)
    branch.delete()
    return Response({"message": "Branch deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def branch_details(request,branch_pk):
    branch = Branch.objects.get(id=branch_pk)
    gst_list = Gst.objects.filter(branch=branch)
    purchase_list = PurchaseInvoice.objects.filter(branch=branch)
    sales_list = SalesInvoice.objects.filter(branch=branch)

    # print(owner_serializer.id)
    gst_serializer = GstSerializer(gst_list,many=True)
    purchase_serializer = PurchaseInvoiceSerializer(purchase_list,many=True)
    sales_serializer = SalesInvoiceSerializer(sales_list,many=True)


    data = {
        "gst": gst_serializer.data,
        "purchase": purchase_serializer.data,
        "sales": sales_serializer.data,
  
    }
    return Response(data)




# *******************Owner details views*************************

 
@api_view(['POST'])
def create_owner(request, pk):
    company = get_object_or_404(Company, id=pk)
    if request.method=="POST":
        owner_serializer = OwnerSerializer(data=request.data)
        if owner_serializer.is_valid():
            owner_serializer.save(company=company)
            return Response({'message': 'Owner created successfully.'}, status=status.HTTP_201_CREATED)
            
        return Response(owner_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_owner(request, pk, owner_pk):
    company = get_object_or_404(Company, id=pk)
    owner = get_object_or_404(OwnerDetails, id=owner_pk)
    # owner_serializer = OwnerSerializer(instance=owner,data=request.data)

    # if request.method=="POST":
    #     if owner_serializer.is_valid():
    #         owner_serializer.save(company=company)
    #         return Response({'message': 'Owner updated successfully.'},owner_serializer.data, status=status.HTTP_201_CREATED)
    owner_serializer = OwnerSerializer(instance=owner,data=request.data)

    if request.method=="POST":
        if owner_serializer.is_valid():
            owner_serializer.save(company=company)
            return Response({'message': 'Owner updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(owner_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='GET':
        # return Response(owner_serializer.initial_data,{'message':"working"})
        owner_serializer_1 = OwnerSerializer(owner)
        return Response(owner_serializer_1.data)


@api_view(['DELETE'])
def delete_owner(request,pk,owner_pk):
    company = get_object_or_404(Company, id=pk)
    owner = get_object_or_404(OwnerDetails, id=owner_pk)
    owner.delete()
    return Response({"message": "Owner deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# ******************** bank details views********************

@api_view(['POST'])
def create_bank_details(request,pk):
    company = get_object_or_404(Company,id=pk)
    if request.method=="POST":
        bank_serializer = BankSerializer(data=request.data)
        if bank_serializer.is_valid():
         
            bank_serializer.save(company=company)
            return Response({'message': 'Bank Details created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(bank_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_bank(request,pk,bank_pk):
    company = get_object_or_404(Company, id=pk)
    bank = get_object_or_404(BankDetails, id=bank_pk)
    bank_serializer = BankSerializer(data=request.data, instance=bank)

    if request.method=="POST":
        if bank_serializer.is_valid():
           
            bank_serializer.save(company=company)
            return Response({'message': 'Bank updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(bank_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
            bank_serializer1 = BankSerializer(bank)
    return Response(bank_serializer1.data)





@api_view(['DELETE'])
def delete_bank(request,pk,bank_pk):
    company = get_object_or_404(Company, id=pk)
    bank = get_object_or_404(BankDetails, id=bank_pk)
    bank.delete()
    return Response({"message": "Bank deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# *******************create aadhar****************
@api_view(['POST'])
def create_aadhar(request, pk):
    company = get_object_or_404(Company, id=pk)
    if request.method=="POST":
        aadhar_serializer = AadharSerializer(data=request.data)
        if aadhar_serializer.is_valid():
         
            aadhar_serializer.save(company=company)
            return Response({'message': 'Udhyam Aadhar created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(aadhar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_aadhar(request, pk, aadhar_pk):
    company = get_object_or_404(Company, id=pk)
    aadhar = get_object_or_404(UdyamAadhar, id=aadhar_pk)
    aadhar_serializer = AadharSerializer(data=request.data, instance=aadhar)

    if request.method == "POST":
        if aadhar_serializer.is_valid():
        
            aadhar_serializer.save(company=company)
            return Response({'message': 'Udhyam Aadhar updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(aadhar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        aadhar_serializer1=AadharSerializer(aadhar)
        return Response(aadhar_serializer1.data)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def delete_aadhar(request, pk, aadhar_pk):
    company = get_object_or_404(Company, id=pk)
    aadhar = get_object_or_404(UdyamAadhar, id=aadhar_pk)
    aadhar.delete()
    return Response({"message": "Udhyam Aadhar deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# ********************tan views**********************
@api_view(['POST'])
def create_tan(request,pk):
    company = get_object_or_404(Company, id=pk)
    if request.method=="POST":
        tan_serializer = TanSerializer(data=request.data)
        if tan_serializer.is_valid():

            tan_serializer.save(company=company)
            return Response({'message': 'Tan created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(tan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_tan(request, pk, tan_pk):
    company = get_object_or_404(Company, id=pk)
    tan = get_object_or_404(Tan, id=tan_pk)
    tan_serializer = TanSerializer(data=request.data, instance=tan)

    if request.method == "POST":
        if tan_serializer.is_valid():
        
            tan_serializer.save(company=company)
            return Response({'message': 'Tan updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(tan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        tan_serializer1=TanSerializer(tan)
    return Response(tan_serializer1.data)



@api_view(['DELETE'])
def delete_tan(request, pk, tan_pk):
    company = get_object_or_404(Company, id=pk)
    tan = get_object_or_404(Tan, id=tan_pk)
    tan.delete()
    return Response({"message": "Tan deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# *******************Ptrc views*******************

@api_view(['POST'])
def create_ptrc(request,pk):
    company = get_object_or_404(Company, id=pk)
    if request.method=="POST":
        ptrc_serializer = PtrcSerializer(data=request.data)
        if ptrc_serializer.is_valid():

            ptrc_serializer.save(company=company)
            return Response({'message': 'Ptrc created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(ptrc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_ptrc(request, pk, ptrc_pk):
    company = get_object_or_404(Company, id=pk)
    ptrc = get_object_or_404(Ptrc, id=ptrc_pk)
    ptrc_serializer = PtrcSerializer(data=request.data, instance=ptrc)

    if request.method == "POST":
        if ptrc_serializer.is_valid():
        
            ptrc_serializer.save(company=company)
            return Response({'message': 'Ptrc updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(ptrc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        ptrc_serializer1=PtrcSerializer(ptrc)
    return Response(ptrc_serializer1.data)


@api_view(['DELETE'])
def delete_ptrc(request, pk, ptrc_pk):
    company = get_object_or_404(Company, id=pk)
    ptrc = get_object_or_404(Ptrc, id=ptrc_pk)
    ptrc.delete()
    return Response({"message": "Ptrc deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



# *******************Ptec views*******************

@api_view(['POST'])
def create_ptec(request,pk):
    company = get_object_or_404(Company, id=pk)
    if request.method=="POST":
        ptec_serializer = PtecSerializer(data=request.data)
        if ptec_serializer.is_valid():

            ptec_serializer.save(company=company)
            return Response({'message': 'Ptec created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(ptec_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_ptec(request, pk, ptec_pk):
    company = get_object_or_404(Company, id=pk)
    ptec = get_object_or_404(Ptec, id=ptec_pk)
    ptec_serializer = PtecSerializer(data=request.data, instance=ptec)

    if request.method == "POST":
        if ptec_serializer.is_valid():
        
            ptec_serializer.save(company=company)
            return Response({'message': 'Ptrc updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(ptec_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        ptec_serializer1=PtecSerializer(ptec)
    return Response(ptec_serializer1.data)


@api_view(['DELETE'])
def delete_ptec(request, pk, ptec_pk):
    company = get_object_or_404(Company, id=pk)
    ptec = get_object_or_404(Ptec, id=ptec_pk)
    ptec.delete()
    return Response({"message": "Ptec deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_pan(request,pk):
    company = get_object_or_404(Company, id=pk)
    if request.method=="POST":
        pan_serializer = PanSerializer(data=request.data)
        if pan_serializer.is_valid():

            pan_serializer.save(company=company)
            return Response({'message': 'Pan created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(pan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_pan(request, pk, pan_pk):
    company = get_object_or_404(Company, id=pk)
    pan = get_object_or_404(Pan, id=pan_pk)
    pan_serializer = PanSerializer(data=request.data, instance=pan)

    if request.method == "POST":
        if pan_serializer.is_valid():
        
            pan_serializer.save(company=company)
            return Response({'message': 'Pan updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(pan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        pan_serializer1=PanSerializer(pan)
    return Response(pan_serializer1.data)

@api_view(['DELETE'])
def delete_pan(request, pk, pan_pk):
    company = get_object_or_404(Company, id=pk)
    pan = get_object_or_404(Pan, id=pan_pk)
    pan.delete()
    return Response({"message": "Pan deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# *************msme views**************

@api_view(['POST'])
def create_msme(request,pk):
    company = get_object_or_404(Company, id=pk)
    if request.method=="POST":
        msme_serializer = MsmeSerializer(data=request.data)
        if msme_serializer.is_valid():

            msme_serializer.save(company=company)
            return Response({'message': 'Msme created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(msme_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_msme(request, pk, msme_pk):
    company = get_object_or_404(Company, id=pk)
    msme = get_object_or_404(Msme, id=msme_pk)
    msme_serializer = MsmeSerializer(data=request.data, instance=msme)

    if request.method == "POST":
        if msme_serializer.is_valid():
        
            msme_serializer.save(company=company)
            return Response({'message': 'Msme updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(msme_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        msme_serializer1=MsmeSerializer(msme)
    return Response(msme_serializer1.data)

@api_view(['DELETE'])
def delete_msme(request, pk, msme_pk):
    company = get_object_or_404(Company, id=pk)
    msme = get_object_or_404(Msme, id=msme_pk)
    msme.delete()
    return Response({"message": "Msme deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# **********************gst branch views**************

@api_view(['POST'])
def create_gst(request,branch_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    gst = Gst.objects.filter(branch=branch)
    if request.method=="POST":
        if len(gst) == 0:
            gst_serializer = GstSerializer(data=request.data)
            if gst_serializer.is_valid():

                gst_serializer.save(branch=branch)
                return Response({'message': 'Gst created successfully.'}, status=status.HTTP_201_CREATED)

            return Response(gst_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'You can create gst only once',})
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_gst(request, branch_pk, gst_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    gst = get_object_or_404(Gst, id=gst_pk)
    gst_serializer = GstSerializer(data=request.data, instance=gst)

    if request.method == "POST":
        if gst_serializer.is_valid():
        
            gst_serializer.save(branch=branch)
            return Response({'message': 'Gst updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(gst_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        gst_serializer1=GstSerializer(gst)
    return Response(gst_serializer1.data)


@api_view(['DELETE'])
def delete_gst(request, branch_pk, gst_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    gst = get_object_or_404(Gst, id=gst_pk)
    gst.delete()
    return Response({"message": "Msme deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# @csrf_exempt
@api_view(['POST','GET'])
def create_sales_invoice(request, branch_pk):
    branch = get_object_or_404(Branch, id=branch_pk)

    company= branch.company
    # branch_gst = GstSerializer.objects.filter(branch=branch)
    if request.method=="GET":
        # branch_v_serializer = VBranchSerializer(data=request.data)
        # mn = 
        gst_no=request.GET.get('mn')
       
        print("gst_no 123:",gst_no)
        party_gst = VendorBranch.objects.filter(vendor__company=company,gst=gst_no).first() or ClientVendor.objects.filter(company=company,pan=gst_no).first()

        if party_gst:
            if hasattr(party_gst, 'gst'):
                # GST field exists in party_gst (VendorBranch)
                vendor1 = party_gst.vendor
                vendor2 = party_gst
                 
                
                # print("branch gst no:",branch_gst)
                # if party_gst[0:2] == branch_gst.gst_number[0:2]:
                #     branch_gst1 = GstSerializer()
                # print("vvvvnnn",vendor2)
                branch_gst = Gst.objects.filter(branch=branch)
                print("party wala:",branch_gst)
                v_branch = VendorSerializer(vendor1)
                v_branch1 = VBranchSerializer(vendor2)
                branch_gst1 = GstSerializer(branch_gst,many=True)
                print("branch gst:",branch_gst1)
                combined_data = {
                'v_branch': v_branch.data,
                'v_branch1': v_branch1.data,
                'branch_gst1':branch_gst1.data
                }
                # print("v branch 1 ka :",v_branch1)
                print("v branch sirf ka :",combined_data)
                return Response(combined_data)
            elif hasattr(party_gst, 'pan'):
                # Pan field exists in party_gst (ClientVendor)
                vendor2 = party_gst
                vendor4=party_gst
                
                v_branch = VendorSerializer(vendor2)
                v_branch3 = VendorSerializer(vendor4)
                combined_data={
                    'v_branch': v_branch.data,
                    'v_branch3': v_branch3.data,
                }
                print("vendor 2 pan ka:",combined_data)
                return Response(combined_data)
            else:
                return Response({'error_message': "Invalid data"})
        else:
            return Response({'error_message': "No vendor found"})
        
    if request.method == 'POST':
        # Deserialize the Purchase Invoice data
        sales_serializer = SalesInvoiceSerializer(data=request.data)

        if sales_serializer.is_valid():
            print("total 123 invoie:",request.data)
            sales_instance = sales_serializer.save(branch=branch)

            # Extract and prepare product data
            # print("requet:",request.data)
            products = []

            for key, value in request.data.items():
                if key.startswith('products'):
                    parts = key.split('[')
                    
                    product_index = int(parts[1][:-1])  # Extract the index from the key without the trailing ']'
                    product_key = parts[2][:-1]  # Extract the inner key without the trailing ']'
                    if len(products) < product_index + 1:
                        products.append({})  # Ensure the products list has space for the current index

                    products[product_index][product_key] = value  # Assign the inner key-value pair to the appropriate product
            print("sales_serializer",sales_serializer)
            for index, product_dict in enumerate(products, start=0):
                product1 = ProductSales.objects.create(
                
                sales_invoice=sales_instance,
                hsn=product_dict.get('hsn', 'No hsn'),
                product_name = product_dict.get('product_name', 'No Product'),
                unit_of_measure=product_dict.get('unit_of_measure', 'No measure'),
                unit=product_dict.get('unit', 'No unit'),
                rate=product_dict.get('rate', 'No rate'),
                gst_per=product_dict.get('gst_per', 'No gst_per'),
                cgst=product_dict.get('cgst', 'No cgst'),
                sgst=product_dict.get('sgst', 'No sgst'),
                taxable_amount=product_dict.get('taxable_amount', 'No amount_receivable'),
    
            )


            return Response({'message': 'Sales Invoice created successfully.', 'id': sales_instance.id}, status=status.HTTP_201_CREATED)

        # Handle validation errors for Purchase Invoice
        return Response({'error': sales_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# ************sales invoice views***************


# @api_view(['POST'])
# def create_sales_invoice(request,branch_pk):
#     branch = get_object_or_404(Branch, id=branch_pk)
#     if request.method=="POST":
#         sales_serializer = SalesInvoiceSerializer(data=request.data)
        
#         if sales_serializer.is_valid():
#             amount = sales_serializer.validated_data.get('amount')
#             cgst = sales_serializer.validated_data.get('cgst')
#             sgst = sales_serializer.validated_data.get('sgst')
#             tds = sales_serializer.validated_data.get('tds')
#             tcs = sales_serializer.validated_data.get('tcs')
#             gst_per = sales_serializer.validated_data.get('gst_per')

#             try:
#                 amount = float(amount)
#                 cgst = float(cgst)
#                 sgst = float(sgst)
#                 tds = float(tds)
#                 tcs = float(tcs)
#                 gst_per = float(gst_per)
#                 print("Amount:", amount)
#                 print("CGST:", cgst)
#                 print("SGST:", sgst)
#                 print("TDS:", tds)
#                 print("TCS:", tcs)
#                 # Calculate in_amount
#                 in_amount = amount + cgst + gst_per + sgst + tcs - tds
#                 print("Calculated in_amount:", in_amount)

#                 # Update the serializer with the calculated in_amount
#                 sales_serializer.validated_data['in_amount'] = in_amount
#                 sales_instance = sales_serializer.save(branch=branch)

#                 return Response({'message': 'Sales Invoice created successfully.', 'id': sales_instance.id}, status=status.HTTP_201_CREATED)
#             except ValueError:
#                 return Response({'error': 'Invalid numeric values in input'}, status=status.HTTP_400_BAD_REQUEST)

#         return Response(sales_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# @csrf_exempt
@api_view(['POST','GET'])
def create_purchase_invoice(request, branch_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    company =branch.company
    # print("abc22:",abc)
    # branch_gst = GstSerializer.objects.filter(branch=branch)
    if request.method=="GET":
        # branch_v_serializer = VBranchSerializer(data=request.data)
        # mn = 
        gst_no = request.GET.get('mn')
        branch_id = request.GET.get('bm')

        print("branch company:",branch_id)
       
        print("gst_no 123:",gst_no)
        party_gst = VendorBranch.objects.filter(vendor__company=company,gst=gst_no).first() or ClientVendor.objects.filter(company=company,pan=gst_no).first()

        if party_gst:
            if hasattr(party_gst, 'gst'):
                # GST field exists in party_gst (VendorBranch)
                vendor1 = party_gst.vendor
                vendor2 = party_gst
                 
                
                # print("branch gst no:",branch_gst)
                # if party_gst[0:2] == branch_gst.gst_number[0:2]:
                #     branch_gst1 = GstSerializer()
                # print("vvvvnnn",vendor2)
                branch_gst = Gst.objects.filter(branch=branch)
                print("party wala:",branch_gst)
                v_branch = VendorSerializer(vendor1)
                v_branch1 = VBranchSerializer(vendor2)
                branch_gst1 = GstSerializer(branch_gst,many=True)
                print("branch gst:",branch_gst1)
                combined_data = {
                'v_branch': v_branch.data,
                'v_branch1': v_branch1.data,
                'branch_gst1':branch_gst1.data
                }
                # print("v branch 1 ka :",v_branch1)
                print("v branch sirf ka :",combined_data)
                return Response(combined_data)
            elif hasattr(party_gst, 'pan'):
                # Pan field exists in party_gst (ClientVendor)
                vendor2 = party_gst
                vendor4=party_gst
                
                v_branch = VendorSerializer(vendor2)
                v_branch3 = VendorSerializer(vendor4)
                combined_data={
                    'v_branch': v_branch.data,
                    'v_branch3': v_branch3.data,
                }
                print("vendor 2 pan ka:",combined_data)
                return Response(combined_data)
            else:
                return Response({'error_message': "Invalid data"})
        else:
            return Response({'error_message': "No vendor found"})
        
    if request.method == 'POST':
        # Deserialize the Purchase Invoice data
        purchase_serializer = PurchaseInvoiceSerializer(data=request.data)

        if purchase_serializer.is_valid():
            print("total invoie:",request.data)
            purchase_instance = purchase_serializer.save(branch=branch)

            # Extract and prepare product data
            # print("requet:",request.data)
            products = []

            for key, value in request.data.items():
                if key.startswith('products'):
                    parts = key.split('[')
                    
                    product_index = int(parts[1][:-1])  # Extract the index from the key without the trailing ']'
                    product_key = parts[2][:-1]  # Extract the inner key without the trailing ']'
                    if len(products) < product_index + 1:
                        products.append({})  # Ensure the products list has space for the current index

                    products[product_index][product_key] = value  # Assign the inner key-value pair to the appropriate product

            # print(products)
            # products2 = list(products)
            # Create ProductDetails instances linked to the PurchaseInvoice
            # print("products 2:",products2)
            # for i in products:
            # for product in products:
            #     for key, value, index in product.items():
            #         print(f"Key: {key}, Value: {value}, index:{index}")
            for index, product_dict in enumerate(products, start=0):
                product1 = ProductDetails.objects.create(
                
                purchase_invoice=purchase_instance,
                # hsn=products[i].get('hsn') if products[0].get('hsn') else 'No HSN',
                hsn=product_dict.get('hsn', 'No hsn'),
                # product_name="watches",
                product_name = product_dict.get('product_name', 'No Product'),
                unit_of_measure=product_dict.get('unit_of_measure', 'No measure'),
                unit=product_dict.get('unit', 'No unit'),
                rate=product_dict.get('rate', 'No rate'),
                gst_per=product_dict.get('gst_per', 'No gst_per'),
                # total_gst=product_dict.get('total_gst', 'No gst'),
                # total_tax_amount=product_dict.get('total_tax_amount', 'No Taxable'),
                cgst=product_dict.get('cgst', 'No cgst'),
                sgst=product_dict.get('sgst', 'No cgst'),
                # sgst=product_dict.get('sgst', 'No cgst'),
                # hsn="24",
                # product_name=products[i].get('product_name') if products[i].get('product_name') else 'No Product',
                # unit_of_measure=products[i].get('unit_of_measure') if products[i].get('unit_of_measure') else 'No unit of measure',
                # ... other fields
            )

            # Calculate and update total_invoice field in Purchase Invoice
            # purchase_instance.calculate_total_invoice()

            return Response({'message': 'Purchase Invoice created successfully.', 'id': purchase_instance.id}, status=status.HTTP_201_CREATED)

        # Handle validation errors for Purchase Invoice
        return Response({'error': purchase_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# ///////////////////////purchase company view//////////////////////////
@api_view(['POST','GET'])
def create_purchase_invoice_company(request,pk):
    company = get_object_or_404(Company, id=pk)
   
    # company =branch.company
    # print("abc22:",abc)
    # branch_gst = GstSerializer.objects.filter(branch=branch)
    # if request.method=="GET":
        # branch_v_serializer = VBranchSerializer(data=request.data)
        # mn = 
        # gst_no=request.GET.get('mn')
        # branch_id=request.GET.get('bm')
        # branch1 =request.GET.get('branch_id')
    if request.method == "GET":
        gst_no = request.GET.get('mn')
        branch_id = request.GET.get('branch_id')
        # branches = branch_id.branch
        # print("mohammed",branches)
        # logger.info(f"GST Number: {gst_no}")
        # logger.info(f"Branch ID: {branch_id}")
        print("branch branch hjk:",branch_id)
        print("company123",company)
        # branch = get_object_or_404(Branch, id=branch1)
       
        print("gst no hj:",gst_no)
        party_gst = VendorBranch.objects.filter(vendor__company=company,gst=gst_no).first() or ClientVendor.objects.filter(company=company,pan=gst_no).first()

        if party_gst:
            if hasattr(party_gst, 'gst'):
                # GST field exists in party_gst (VendorBranch)
                vendor1 = party_gst.vendor
                vendor2 = party_gst
                 
                
                # print("branch gst no:",branch_gst)
                # if party_gst[0:2] == branch_gst.gst_number[0:2]:
                #     branch_gst1 = GstSerializer()
                # print("vvvvnnn",vendor2)
                print("hhhhhhhhhhhhh",branch_id)
                branch_gst = Gst.objects.filter(branch=branch_id)
                print("party wala:",branch_gst)
                v_branch = VendorSerializer(vendor1)
                v_branch1 = VBranchSerializer(vendor2)
                branch_gst1 = GstSerializer(branch_gst,many=True)
                print("atul bhai",branch_gst1)
                print("branch gst:",branch_gst1)
                combined_data = {
                'v_branch': v_branch.data,
                'v_branch1': v_branch1.data,
                'branch_gst1':branch_gst1.data
                }
                # print("v branch 1 ka :",v_branch1)
                print("v branch sirf ka :",combined_data)
                return Response(combined_data)
            elif hasattr(party_gst, 'pan'):
                # Pan field exists in party_gst (ClientVendor)
                vendor2 = party_gst
                vendor4=party_gst
                
                v_branch = VendorSerializer(vendor2)
                v_branch3 = VendorSerializer(vendor4)
                combined_data={
                    'v_branch': v_branch.data,
                    'v_branch3': v_branch3.data,
                }
                print("vendor 2 pan ka:",combined_data)
                return Response(combined_data)
            else:
                return Response({'error_message': "Invalid data"})
        else:
            return Response({'error_message': "No vendor found"})
        
    if request.method == 'POST':
        # Deserialize the Purchase Invoice data
        purchase_serializer = PurchaseCompanySerializer(data=request.data)

        if purchase_serializer.is_valid():
            print("total invoie:",request.data)
            branch = purchase_serializer.validated_data.get('branch')
            print("gijo",branch)
            purchase_instance = purchase_serializer.save(branch=branch)

            # Extract and prepare product data.
            # print("requet:",request.data)
            products = []

            for key, value in request.data.items():
                if key.startswith('products'):
                    parts = key.split('[')
                    
                    product_index = int(parts[1][:-1])  # Extract the index from the key without the trailing ']'
                    product_key = parts[2][:-1]  # Extract the inner key without the trailing ']'
                    if len(products) < product_index + 1:
                        products.append({})  # Ensure the products list has space for the current index

                    products[product_index][product_key] = value  # Assign the inner key-value pair to the appropriate product

            # print(products)
            # products2 = list(products)
            # Create ProductDetails instances linked to the PurchaseInvoice
            # print("products 2:",products2)
            # for i in products:
            # for product in products:
            #     for key, value, index in product.items():
            #         print(f"Key: {key}, Value: {value}, index:{index}")
            for index, product_dict in enumerate(products, start=0):
                product1 = ProductDetails.objects.create(
                
                purchase_invoice=purchase_instance,
                # hsn=products[i].get('hsn') if products[0].get('hsn') else 'No HSN',
                hsn=product_dict.get('hsn', 'No hsn'),
                # product_name="watches",
                product_name = product_dict.get('product_name', 'No Product'),
                unit_of_measure=product_dict.get('unit_of_measure', 'No measure'),
                unit=product_dict.get('unit', 'No unit'),
                rate=product_dict.get('rate', 'No rate'),
                gst_per=product_dict.get('gst_per', 'No gst_per'),
                # total_gst=product_dict.get('total_gst', 'No gst'),
                # total_tax_amount=product_dict.get('total_tax_amount', 'No Taxable'),
                cgst=product_dict.get('cgst', '0'),
                sgst=product_dict.get('sgst', '0'),
                igst=product_dict.get('igst', '0'),
                taxable_amount=product_dict.get('taxable_amount', '0')
                # hsn="24",
                # product_name=products[i].get('product_name') if products[i].get('product_name') else 'No Product',
                # unit_of_measure=products[i].get('unit_of_measure') if products[i].get('unit_of_measure') else 'No unit of measure',
                # ... other fields
            )

            # Calculate and update total_invoice field in Purchase Invoice
            # purchase_instance.calculate_total_invoice()

            return Response({'message': 'Purchase Invoice created successfully.', 'id': purchase_instance.id}, status=status.HTTP_201_CREATED)

        # Handle validation errors for Purchase Invoice
        return Response({'error': purchase_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# //////////////////purchase company view ends here///////////////////////// 



@api_view(['POST','GET'])
def update_sales_invoice(request, branch_pk, sales_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    sales = get_object_or_404(SalesInvoice, id=sales_pk)
    sales_serializer = SalesInvoiceSerializer(data=request.data, instance=sales)

    if request.method=="POST":
        # sales_serializer = SalesInvoiceSerializer(data=request.data)
        
        if sales_serializer.is_valid():
            amount = sales_serializer.validated_data.get('amount')
            cgst = sales_serializer.validated_data.get('cgst')
            sgst = sales_serializer.validated_data.get('sgst')
            tds = sales_serializer.validated_data.get('tds')
            tcs = sales_serializer.validated_data.get('tcs')
            gst_per = sales_serializer.validated_data.get('gst_per')

            try:
                amount = float(amount)
                cgst = float(cgst)
                sgst = float(sgst)
                tds = float(tds)
                tcs = float(tcs)
                gst_per = float(gst_per)
                print("Amount:", amount)
                print("CGST:", cgst)
                print("SGST:", sgst)
                print("TDS:", tds)
                print("TCS:", tcs)
                # Calculate in_amount
                in_amount = amount + cgst + gst_per + sgst + tcs - tds
                print("Calculated in_amount:", in_amount)

                # Update the serializer with the calculated in_amount
                sales_serializer.validated_data['in_amount'] = in_amount
                sales_instance = sales_serializer.save(branch=branch)

                return Response({'message': 'Sales Invoice created successfully.', 'id': sales_instance.id}, status=status.HTTP_201_CREATED)
            except ValueError:
                return Response({'error': 'Invalid numeric values in input'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(sales_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        sales_serializer1=SalesInvoiceSerializer(sales)
    return Response(sales_serializer1.data)


@api_view(['DELETE'])
def delete_sales_invoice(request, branch_pk, sales_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    sales = get_object_or_404(SalesInvoice, id=sales_pk)
    sales.delete()
    return Response({"message": "Sales Invoice deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# ***************credit note****************
@api_view(['POST','GET'])
def create_credit_note(request, branch_pk,sales_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    sales = get_object_or_404(SalesInvoice, id=sales_pk)
    company =branch.company
    # print("abc22:",abc)
    # branch_gst = GstSerializer.objects.filter(branch=branch)
    if request.method=="GET":
        # branch_v_serializer = VBranchSerializer(data=request.data)
        # mn = 
        gst_no=request.GET.get('mn')
       
        print("gst_no 123:",gst_no)
        party_gst = VendorBranch.objects.filter(vendor__company=company,gst=gst_no).first() or ClientVendor.objects.filter(company=company,pan=gst_no).first()

        if party_gst:
            if hasattr(party_gst, 'gst'):
                # GST field exists in party_gst (VendorBranch)
                vendor1 = party_gst.vendor
                vendor2 = party_gst
                 
                
                # print("branch gst no:",branch_gst)
                # if party_gst[0:2] == branch_gst.gst_number[0:2]:
                #     branch_gst1 = GstSerializer()
                # print("vvvvnnn",vendor2)
                branch_gst = Gst.objects.filter(branch=branch)
                print("party wala:",branch_gst)
                v_branch = VendorSerializer(vendor1)
                v_branch1 = VBranchSerializer(vendor2)
                branch_gst1 = GstSerializer(branch_gst,many=True)
                print("branch gst:",branch_gst1)
                combined_data = {
                'v_branch': v_branch.data,
                'v_branch1': v_branch1.data,
                'branch_gst1':branch_gst1.data
                }
                # print("v branch 1 ka :",v_branch1)
                print("v branch sirf ka :",combined_data)
                return Response(combined_data)
            elif hasattr(party_gst, 'pan'):
                # Pan field exists in party_gst (ClientVendor)
                vendor2 = party_gst
                vendor4=party_gst
                
                v_branch = VendorSerializer(vendor2)
                v_branch3 = VendorSerializer(vendor4)
                combined_data={
                    'v_branch': v_branch.data,
                    'v_branch3': v_branch3.data,
                }
                print("vendor 2 pan ka:",combined_data)
                return Response(combined_data)
            else:
                return Response({'error_message': "Invalid data"})
        else:
            return Response({'error_message': "No vendor found"})
        
    if request.method == 'POST':
        # Deserialize the Purchase Invoice data
        sales_serializer = CreditNoteSerializer(data=request.data)

        if sales_serializer.is_valid():
            print("total invoie:",request.data)
            sales_instance = sales_serializer.save(branch=branch, sales_invoice=sales)
            print("pbb",sales_instance)
            # Extract and prepare product data
            # print("requet:",request.data)
            products = []

            for key, value in request.data.items():
                if key.startswith('products'):
                    parts = key.split('[')
                    
                    product_index = int(parts[1][:-1])  # Extract the index from the key without the trailing ']'
                    product_key = parts[2][:-1]  # Extract the inner key without the trailing ']'
                    if len(products) < product_index + 1:
                        products.append({})  # Ensure the products list has space for the current index

                    products[product_index][product_key] = value  # Assign the inner key-value pair to the appropriate product

            # print(products)
            # products2 = list(products)
            # Create ProductDetails instances linked to the PurchaseInvoice
            # print("products 2:",products2)
            # for i in products:
            # for product in products:
            #     for key, value, index in product.items():
            #         print(f"Key: {key}, Value: {value}, index:{index}")
            for index, product_dict in enumerate(products, start=0):
                product1 = CreditProduct.objects.create(
                
                credit_note=sales_instance,
                # hsn=products[i].get('hsn') if products[0].get('hsn') else 'No HSN',
                hsn=product_dict.get('hsn', 'No hsn'),
                # product_name="watches",
                product_name = product_dict.get('product_name', 'No Product'),
                unit_of_measure=product_dict.get('unit_of_measure', 'No measure'),
                unit=product_dict.get('unit', 'No unit'),
                rate=product_dict.get('rate', 'No rate'),
                gst_per=product_dict.get('gst_per', 'No gst_per'),
                cgst=product_dict.get('cgst', '0'),
                sgst=product_dict.get('sgst', '0'),
                igst=product_dict.get('igst', '0'),
                taxable_amount=product_dict.get('taxable_amount', '0'),
                # hsn="24",
                # product_name=products[i].get('product_name') if products[i].get('product_name') else 'No Product',
                # unit_of_measure=products[i].get('unit_of_measure') if products[i].get('unit_of_measure') else 'No unit of measure',
                # ... other fields
            )

            # Calculate and update total_invoice field in Purchase Invoice
            # purchase_instance.calculate_total_invoice()

            return Response({'message': 'Purchase Invoice created successfully.', 'id': sales_instance.id}, status=status.HTTP_201_CREATED)

        # Handle validation errors for Purchase Invoice
        return Response({'error': sales_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['POST','GET'])
def update_credit_note(request, branch_pk, sales_pk,cr_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    sales = get_object_or_404(SalesInvoice, id=sales_pk)
    credit = get_object_or_404(CreditNote, id=cr_pk, branch=branch, sales_in=sales)
    cr_note__serializer = CreditNoteSerializer(data=request.data, instance=credit)

    if request.method == "POST":
        if cr_note__serializer.is_valid():
        
            cr_note__serializer.save()
            return Response({'message': 'Credit Note updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(cr_note__serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        cr_note__serializer1=CreditNoteSerializer(credit)
    return Response(cr_note__serializer1.data)


@api_view(['DELETE'])
def delete_credit_note(request, branch_pk, sales_pk,cr_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    sales = get_object_or_404(SalesInvoice, id=sales_pk)
    credit = get_object_or_404(CreditNote, id=cr_pk, branch=branch, sales_in=sales)

    credit.delete()
    return Response({"message": "Credit Note deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def credit_note_view(request,branch_pk,sales_pk):
    branch = Branch.objects.get(id=branch_pk)
    sales = SalesInvoice.objects.get(id=sales_pk)
    cr_note = CreditNote.objects.filter(branch=branch,sales_invoice=sales)

    # print(owner_serializer.id)
    cr_note_serializer = CreditNoteSerializer(cr_note,many=True)


    data = {
        "credit": cr_note_serializer.data,
  
    }
    return Response(data)

# *************purchase invoice views*************
# @api_view(['POST'])
# def create_purchase_invoice(request, branch_pk):
#     branch = get_object_or_404(Branch, id=branch_pk)
#     gst = Gst.objects.filter(branch=branch).first()
    
#     if request.method == 'POST':
#         purchase_serializer = PurchaseInvoiceSerializer(data=request.data)

#         if purchase_serializer.is_valid():
#             # Extract values from the validated data
#             # cgst = purchase_serializer.validated_data.get('cgst')
#             # sgst = purchase_serializer.validated_data.get('sgst')
#             tds = purchase_serializer.validated_data.get('tds')
#             tcs = purchase_serializer.validated_data.get('tcs')
#             gst_per = purchase_serializer.validated_data.get('gst_per')
#             purchase_gst_no = purchase_serializer.validated_data.get('gst_no')
#             unit = purchase_serializer.validated_data.get('unit')
#             rate = purchase_serializer.validated_data.get('rate')
#             gst_no = purchase_serializer.validated_data.get('gst_no')
#             invoice_type = purchase_serializer.validated_data.get('invoice_type')
#             # taxable_amount = purchase_serializer.validated_data.get('taxable_amount')


#             party = VendorBranch.objects.filter(gst=gst_no).first()
#             if party:
#                 if party.gst == gst_no:
#                     party_name = party.vendor.name
#                     purchase_serializer.validated_data['party_name'] = party_name
#                     print("party11==", party.gst)
#                     print("a147852369==", party.vendor.name)
#                 else:
#                     purchase_serializer.validated_data['party_name'] = "no matching found"
#             else:
#                 purchase_serializer.validated_data['party_name'] = "no matching found"


#             try:
#                 total_invoice = 0
#                 # cgst = float(cgst)
#                 # sgst = float(sgst)
#                 # tds = float(tds)
#                 # tcs = float(tcs)
#                 if gst_per:
#                     gst_per = float(gst_per)
#                 else:
#                     gst_per=0
#                 unit = float(unit)
#                 rate = float(rate)
#                 # taxable_amount = float(taxable_amount)

#                 # Calculate in_amount based on the first two letters of GST number
#                 taxable_amount = unit*rate
#                 purchase_serializer.validated_data['taxable_amount'] = taxable_amount
#                 party1 = ClientVendor.objects.filter(pan=gst_no).first()
#                 if gst and gst.gst_number[:2] == purchase_gst_no[:2]:
                    
#                     if invoice_type == "nill-rated" or "export":
#                         # purchase_serializer.validated_data['gst_per'] = 0
#                         taxable_amount = unit*rate
#                         purchase_serializer.validated_data['taxable_amount'] = taxable_amount
#                         total_invoice = unit*rate
#                         purchase_serializer.validated_data['total_invoice'] = total_invoice

                       
#                         cgst=0
#                         sgst=0
#                     else:
#                         cgst = taxable_amount * gst_per / 2 / 100
#                         sgst = taxable_amount * gst_per / 2 / 100

#                         purchase_serializer.validated_data['cgst'] = cgst
#                         purchase_serializer.validated_data['sgst'] = sgst
#                         total_invoice=taxable_amount + cgst + sgst

#                 elif gst_no == party1.pan:
#                     if invoice_type=="unregistered-nonlocal":
#                         igst = taxable_amount * gst_per/100
#                         purchase_serializer.validated_data['igst'] = igst
#                         total_invoice=taxable_amount + igst
#                     elif invoice_type=="unregistered-local":
#                         cgst = taxable_amount * gst_per / 2 / 100
#                         sgst = taxable_amount * gst_per / 2 / 100

#                         purchase_serializer.validated_data['cgst'] = cgst
#                         purchase_serializer.validated_data['sgst'] = sgst
#                         total_invoice=taxable_amount + cgst + sgst
#                     else:
#                         taxable_amount = unit*rate
#                         purchase_serializer.validated_data['taxable_amount'] = taxable_amount
#                         total_invoice = unit*rate
#                         purchase_serializer.validated_data['total_invoice'] = total_invoice

                       
#                         cgst=0
#                         sgst=0


#                 else:
#                         igst = taxable_amount * gst_per
#                         purchase_serializer.validated_data['igst'] = igst
#                         total_invoice=taxable_amount + igst


                    
#                 # Update the serializer with the calculated in_amount
#                 purchase_serializer.validated_data['total_invoice'] = total_invoice
#                 if tds is not None:

#                     amount_receivable= (total_invoice - tds)
#                 else:
#                     amount_receivable= (total_invoice + tcs)
#                 purchase_serializer.validated_data['amount_receivable'] = amount_receivable

                

#                 # Save the instance
#                 purchase_instance = purchase_serializer.save(branch=branch)

#                 print("unit",unit)
#                 print("rate",rate)
#                 print("gst_per",gst_per)
                
#                 print("taxable_amount",taxable_amount)
#                 # print("cgst",cgst)
#                 # print("sgst",sgst)
#                 # print("igst",igst)
#                 print("total_invoice",total_invoice)
#                 print("tcs",tcs)
#                 print("tds",tds)
#                 print("amount_receivable",amount_receivable)

#                 return Response({'message': 'Purchase Invoice created successfully.', 'id': purchase_instance.id}, status=status.HTTP_201_CREATED)
#             except ValueError:
#                 return Response({'error': 'Invalid numeric values in input'}, status=status.HTTP_400_BAD_REQUEST)

#         return Response(purchase_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



# @api_view(['POST'])
# def create_purchase_invoice(request, branch_pk):
#     branch = get_object_or_404(Branch, id=branch_pk)
#     gst = Gst.objects.filter(branch=branch).first()

#     if request.method == 'POST':
#         purchase_serializer = PurchaseInvoiceSerializer(data=request.data)

#         if purchase_serializer.is_valid():
#             # Save the instance
#             purchase_instance = purchase_serializer.save(branch=branch)

#             # Handle Products
#             products_data = request.data.get('products', [])
#             for product_data in products_data:
#                 product_data['purchase_invoice'] = purchase_instance.id
#                 product_serializer = ProductDetailsSerializer(data=product_data)
#                 if product_serializer.is_valid():
#                     product_serializer.save()
#                 else:
#                     # Handle validation errors for individual products
#                     return Response({'error': product_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#             return Response({'message': 'Purchase Invoice created successfully.', 'id': purchase_instance.id}, status=status.HTTP_201_CREATED)

#         return Response(purchase_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



# @api_view(['POST'])
# def create_purchase_invoice(request,branch_pk):
#     branch = get_object_or_404(Branch, id=branch_pk)
#     if request.method=="POST":
#         purchase_serializer = PurchaseInvoiceSerializer(data=request.data)
#         if purchase_serializer.is_valid():

#             purchase_serializer.save(branch=branch)
#             return Response({'message': 'Purchase Invoice created successfully.'}, status=status.HTTP_201_CREATED)

#         return Response(purchase_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['POST','GET'])
def update_purchase_invoice(request, branch_pk, purchase_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    purchase = get_object_or_404(PurchaseInvoice, id=purchase_pk)
    purchase_serializer = PurchaseInvoiceSerializer(data=request.data, instance=purchase)

    if request.method == 'POST':
        # purchase_serializer = PurchaseInvoiceSerializer(data=request.data)

        if purchase_serializer.is_valid():
            # Extract values from the validated data
            amount = purchase_serializer.validated_data.get('amount')
            cgst = purchase_serializer.validated_data.get('cgst')
            sgst = purchase_serializer.validated_data.get('sgst')
            tds = purchase_serializer.validated_data.get('tds')
            tcs = purchase_serializer.validated_data.get('tcs')
            gst_per = purchase_serializer.validated_data.get('gst_per')

            try:
                amount = float(amount)
                cgst = float(cgst)
                sgst = float(sgst)
                tds = float(tds)
                tcs = float(tcs)
                gst_per = float(gst_per)
                print("Amount:", amount)
                print("CGST:", cgst)
                print("SGST:", sgst)
                print("TDS:", tds)
                print("TCS:", tcs)
                # Calculate in_amount
                in_amount = amount + cgst + gst_per + sgst + tcs - tds
                print("Calculated in_amount:", in_amount)

                # Update the serializer with the calculated in_amount
                purchase_serializer.validated_data['in_amount'] = in_amount

                # Save the instance
                purchase_instance = purchase_serializer.save(branch=branch)

                return Response({'message': 'Purchase Invoice created successfully.', 'id': purchase_instance.id}, status=status.HTTP_201_CREATED)
            except ValueError:
                return Response({'error': 'Invalid numeric values in input'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(purchase_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        purchase_serializer1=PurchaseInvoiceSerializer(purchase)
    return Response(purchase_serializer1.data)


@api_view(['DELETE'])
def delete_purchase_invoice(request, branch_pk, purchase_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    purchase = get_object_or_404(PurchaseInvoice, id=purchase_pk)
    purchase.delete()
    return Response({"message": "Purchase Invoice deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



# **************debit note************
@api_view(['POST','GET'])
def create_debit_note(request, branch_pk,purchase_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    purchase = get_object_or_404(PurchaseInvoice, id=purchase_pk)
    company =branch.company
    # print("abc22:",abc)
    # branch_gst = GstSerializer.objects.filter(branch=branch)
    if request.method=="GET":
        # branch_v_serializer = VBranchSerializer(data=request.data)
        # mn = 
        gst_no=request.GET.get('mn')
       
        print("gst_no 123:",gst_no)
        party_gst = VendorBranch.objects.filter(vendor__company=company,gst=gst_no).first() or ClientVendor.objects.filter(company=company,pan=gst_no).first()

        if party_gst:
            if hasattr(party_gst, 'gst'):
                # GST field exists in party_gst (VendorBranch)
                vendor1 = party_gst.vendor
                vendor2 = party_gst
                 
                
                # print("branch gst no:",branch_gst)
                # if party_gst[0:2] == branch_gst.gst_number[0:2]:
                #     branch_gst1 = GstSerializer()
                # print("vvvvnnn",vendor2)
                branch_gst = Gst.objects.filter(branch=branch)
                print("party wala:",branch_gst)
                v_branch = VendorSerializer(vendor1)
                v_branch1 = VBranchSerializer(vendor2)
                branch_gst1 = GstSerializer(branch_gst,many=True)
                print("branch gst:",branch_gst1)
                combined_data = {
                'v_branch': v_branch.data,
                'v_branch1': v_branch1.data,
                'branch_gst1':branch_gst1.data
                }
                # print("v branch 1 ka :",v_branch1)
                print("v branch sirf ka :",combined_data)
                return Response(combined_data)
            elif hasattr(party_gst, 'pan'):
                # Pan field exists in party_gst (ClientVendor)
                vendor2 = party_gst
                vendor4=party_gst
                
                v_branch = VendorSerializer(vendor2)
                v_branch3 = VendorSerializer(vendor4)
                combined_data={
                    'v_branch': v_branch.data,
                    'v_branch3': v_branch3.data,
                }
                print("vendor 2 pan ka:",combined_data)
                return Response(combined_data)
            else:
                return Response({'error_message': "Invalid data"})
        else:
            return Response({'error_message': "No vendor found"})
        
    if request.method == 'POST':
        # Deserialize the Purchase Invoice data
        purchase_serializer = DebitNoteSerializer(data=request.data)

        if purchase_serializer.is_valid():
            print("total invoie:",request.data)
            purchase_instance = purchase_serializer.save(branch=branch, purchase_invoice=purchase)
            print("pbb",purchase_instance)
            # Extract and prepare product data
            # print("requet:",request.data)
            products = []

            for key, value in request.data.items():
                if key.startswith('products'):
                    parts = key.split('[')
                    
                    product_index = int(parts[1][:-1])  # Extract the index from the key without the trailing ']'
                    product_key = parts[2][:-1]  # Extract the inner key without the trailing ']'
                    if len(products) < product_index + 1:
                        products.append({})  # Ensure the products list has space for the current index

                    products[product_index][product_key] = value  # Assign the inner key-value pair to the appropriate product

            # print(products)
            # products2 = list(products)
            # Create ProductDetails instances linked to the PurchaseInvoice
            # print("products 2:",products2)
            # for i in products:
            # for product in products:
            #     for key, value, index in product.items():
            #         print(f"Key: {key}, Value: {value}, index:{index}")
            for index, product_dict in enumerate(products, start=0):
                product1 = DebitProduct.objects.create(
                
                debit_note=purchase_instance,
                # hsn=products[i].get('hsn') if products[0].get('hsn') else 'No HSN',
                hsn=product_dict.get('hsn', 'No hsn'),
                # product_name="watches",
                product_name = product_dict.get('product_name', 'No Product'),
                unit_of_measure=product_dict.get('unit_of_measure', 'No measure'),
                unit=product_dict.get('unit', 'No unit'),
                rate=product_dict.get('rate', 'No rate'),
                gst_per=product_dict.get('gst_per', 'No gst_per'),
                cgst=product_dict.get('cgst', '0'),
                sgst=product_dict.get('sgst', '0'),
                igst=product_dict.get('igst', '0'),
                taxable_amount=product_dict.get('taxable_amount', '0'),
                # hsn="24",
                # product_name=products[i].get('product_name') if products[i].get('product_name') else 'No Product',
                # unit_of_measure=products[i].get('unit_of_measure') if products[i].get('unit_of_measure') else 'No unit of measure',
                # ... other fields
            )

            # Calculate and update total_invoice field in Purchase Invoice
            # purchase_instance.calculate_total_invoice()

            return Response({'message': 'Purchase Invoice created successfully.', 'id': purchase_instance.id}, status=status.HTTP_201_CREATED)

        # Handle validation errors for Purchase Invoice
        return Response({'error': purchase_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['POST','GET'])
def update_debit_note(request, branch_pk, purchase_pk,db_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    purchase = get_object_or_404(PurchaseInvoice, id=purchase_pk)
    debit = get_object_or_404(DebitNote, id=db_pk, branch=branch, purchase_in=purchase)
    db_note__serializer = DebitNoteSerializer(data=request.data, instance=debit)

    if request.method == "POST":
        if db_note__serializer.is_valid():
        
            db_note__serializer.save()
            return Response({'message': 'Debit Note updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(db_note__serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        db_note__serializer1=DebitNoteSerializer(debit)
    return Response(db_note__serializer1.data)


@api_view(['DELETE'])
def delete_debit_note(request, branch_pk, purchase_pk,db_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    purchase = get_object_or_404(PurchaseInvoice, id=purchase_pk)
    debit = get_object_or_404(DebitNote, id=db_pk, branch=branch, purchase_in=purchase)

    debit.delete()
    return Response({"message": "Debit Note deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def debit_note_view(request,branch_pk,purchase_pk):
    branch = Branch.objects.get(id=branch_pk)
    purchase = PurchaseInvoice.objects.get(id=purchase_pk)
    db_note = DebitNote.objects.filter(branch=branch,purchase_invoice=purchase)

    # print(owner_serializer.id)
    db_note_serializer = DebitNoteSerializer(db_note,many=True)


    data = {
        "debit": db_note_serializer.data,
  
    }
    return Response(data)

# ******************bank statement*****************

@api_view(['POST'])
def create_bank_statement(request,pk):
    company = get_object_or_404(Company, id=pk)
    if request.method=="POST":
        bank_statement_serializer = BankStatementSerializer(data=request.data)
        if bank_statement_serializer.is_valid():

            bank_statement_serializer.save(company=company)
            return Response({'message': 'Bank Statement created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(bank_statement_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['POST','GET'])
def update_bank_statement(request, pk, bs_pk):
    company = get_object_or_404(Company, id=pk)
    bank_statement = get_object_or_404(BankStatement, id=bs_pk)
    bs_serializer = BankStatementSerializer(data=request.data, instance=bank_statement)

    if request.method == "POST":
        if bs_serializer.is_valid():
        
            bs_serializer.save(company=company)
            return Response({'message': 'Bank Statement updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(bs_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        bs_serializer1=BankStatementSerializer(bank_statement)
    return Response(bs_serializer1.data)


@api_view(['DELETE'])
def delete_bank_statement(request, pk, bs_pk):
    company = get_object_or_404(Company, id=pk)
    bank_statement = get_object_or_404(BankStatement, id=bs_pk)
    bank_statement.delete()
    return Response({"message": "Bank Statement deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# *************investment certificate******************

@api_view(['POST'])
def create_interest_certificate(request,pk):
    company = get_object_or_404(Company, id=pk)
    if request.method=="POST":
        interest_certificate_serializer = InterestCertificateSerializer(data=request.data)
        if interest_certificate_serializer.is_valid():

            interest_certificate_serializer.save(company=company)
            return Response({'message': 'Interest Certificate created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(interest_certificate_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_interest_certificate(request, pk, ic_pk):
    company = get_object_or_404(Company, id=pk)
    interest_certificate = get_object_or_404(InterestCertificate, id=ic_pk)
    ic_serializer = InterestCertificateSerializer(data=request.data, instance=interest_certificate)

    if request.method == "POST":
        if ic_serializer.is_valid():
        
            ic_serializer.save(company=company)
            return Response({'message': 'Interest updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(ic_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        ic_serializer1=InterestCertificateSerializer(interest_certificate)
    return Response(ic_serializer1.data)


@api_view(['DELETE'])
def delete_interest_certificate(request, pk, ic_pk):
    company = get_object_or_404(Company, id=pk)
    interest_certificate = get_object_or_404(InterestCertificate, id=ic_pk)
    interest_certificate.delete()
    return Response({"message": "Interest Certificate deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# *************Asset Purchased******************

@api_view(['POST'])
def create_asset_purchased(request,pk):
    company = get_object_or_404(Company, id=pk)
    if request.method=="POST":
        asset_purchased_serializer = AssetsPurchasedSerializer(data=request.data)
        if asset_purchased_serializer.is_valid():

            asset_purchased_serializer.save(company=company)
            return Response({'message': 'Asset Purchased created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(asset_purchased_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_asset_purchased(request, pk, ap_pk):
    company = get_object_or_404(Company, id=pk)
    asset_purchased = get_object_or_404(AssetsPurchasedBill, id=ap_pk)
    ap_serializer = AssetsPurchasedSerializer(data=request.data, instance=asset_purchased)

    if request.method == "POST":
        if ap_serializer.is_valid():
        
            ap_serializer.save(company=company)
            return Response({'message': 'Asset Purchased successfully.'}, status=status.HTTP_201_CREATED)
        return Response(ap_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        ap_serializer1=AssetsPurchasedSerializer(asset_purchased)
    return Response(ap_serializer1.data)

@api_view(['DELETE'])
def delete_asset_purchased(request, pk, ap_pk):
    company = get_object_or_404(Company, id=pk)
    asset_purchased = get_object_or_404(AssetsPurchasedBill, id=ap_pk)
    asset_purchased.delete()
    return Response({"message": "Asset Purchased deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



# *******************loan voucher*******************

@api_view(['POST'])
def create_loan_voucher(request,pk):
    company = get_object_or_404(Company, id=pk)
    if request.method=="POST":
        loan_voucher_serializer = LoanVoucherSerializer(data=request.data)
        if loan_voucher_serializer.is_valid():

            loan_voucher_serializer.save(company=company)
            return Response({'message': 'Loan Voucher created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(loan_voucher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['POST','GET'])
def update_loan_voucher(request, pk, lv_pk):
    company = get_object_or_404(Company, id=pk)
    loan_voucher = get_object_or_404(LoanVoucher, id=lv_pk)
    lv_serializer = LoanVoucherSerializer(data=request.data, instance=loan_voucher)

    if request.method == "POST":
        if lv_serializer.is_valid():
        
            lv_serializer.save(company=company)
            return Response({'message': 'Loan Voucher successfully.'}, status=status.HTTP_201_CREATED)
        return Response(lv_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        lv_serializer1=LoanVoucherSerializer(loan_voucher)
    return Response(lv_serializer1.data)


@api_view(['DELETE'])
def delete_loan_voucher(request, pk, lv_pk):
    company = get_object_or_404(Company, id=pk)
    loan_voucher = get_object_or_404(LoanVoucher, id=lv_pk)
    loan_voucher.delete()
    return Response({"message": "Asset Purchased deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# *******************Tds Certificate*******************

@api_view(['POST'])
def create_tds_certificate(request,pk):
    company = get_object_or_404(Company, id=pk)
    if request.method=="POST":
        tds_certificate_serializer = TdsCertificateSerializer(data=request.data)
        if tds_certificate_serializer.is_valid():

            tds_certificate_serializer.save(company=company)
            return Response({'message': 'Tds Certificate created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(tds_certificate_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_tds_certificate(request, pk, tc_pk):
    company = get_object_or_404(Company, id=pk)
    tds_certificate = get_object_or_404(TdsCertificate, id=tc_pk)
    tc_serializer = TdsCertificateSerializer(data=request.data, instance=tds_certificate)

    if request.method == "POST":
        if tc_serializer.is_valid():
        
            tc_serializer.save(company=company)
            return Response({'message': 'Tds Certificate successfully.'}, status=status.HTTP_201_CREATED)
        return Response(tc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        tc_serializer1=TdsCertificateSerializer(tds_certificate)
    return Response(tc_serializer1.data)


@api_view(['DELETE'])
def delete_tds_certificate(request, pk, tc_pk):
    company = get_object_or_404(Company, id=pk)
    tds_certificate = get_object_or_404(TdsCertificate, id=tc_pk)
    tds_certificate.delete()
    return Response({"message": "Tds Certificate deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# *******************As26*******************

@api_view(['POST'])
def create_as26(request,pk):
    company = get_object_or_404(Company, id=pk)
    if request.method=="POST":
        as26_serializer = As26Serializer(data=request.data)
        if as26_serializer.is_valid():

            as26_serializer.save(company=company)
            return Response({'message': 'As26 created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(as26_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_as26(request, pk, as_pk):
    company = get_object_or_404(Company, id=pk)
    as26 = get_object_or_404(As26, id=as_pk)
    as26_serializer = As26Serializer(data=request.data, instance=as26)

    if request.method == "POST":
        if as26_serializer.is_valid():
        
            as26_serializer.save(company=company)
            return Response({'message': 'As26 updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(as26_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        as26_serializer1=As26Serializer(as26)
    return Response(as26_serializer1.data)

@api_view(['DELETE'])
def delete_as26(request, pk, as_pk):
    company = get_object_or_404(Company, id=pk)
    as26 = get_object_or_404(As26, id=as_pk)
    as26.delete()
    return Response({"message": "As26 deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# ***************investment statement**************

@api_view(['POST'])
def create_investment(request,pk):
    company = get_object_or_404(Company, id=pk)
    if request.method=="POST":
        investment_serializer = InvestmentSerializer(data=request.data)
        if investment_serializer.is_valid():

            investment_serializer.save(company=company)
            return Response({'message': 'Investment Statement created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(investment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['POST','GET'])
def update_investment(request, pk, is_pk):
    company = get_object_or_404(Company, id=pk)
    investment = get_object_or_404(InvestmentStatement, id=is_pk)
    investment_serializer = InvestmentSerializer(data=request.data, instance=investment)

    if request.method == "POST":
        if investment_serializer.is_valid():
        
            investment_serializer.save(company=company)
            return Response({'message': 'Investment Statement updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(investment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        investment_serializer1=InvestmentSerializer(investment)
    return Response(investment_serializer1.data)

@api_view(['DELETE'])
def delete_investment(request, pk, is_pk):
    company = get_object_or_404(Company, id=pk)
    investment = get_object_or_404(InvestmentStatement, id=is_pk)
    investment.delete()
    return Response({"message": "Investment Statement deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# ****************income tax return***************** 

@api_view(['POST'])
def create_tax_return(request,pk):
    company = get_object_or_404(Company, id=pk)
    if request.method=="POST":
        tax_return_serializer = TaxReturnSerializer(data=request.data)
        if tax_return_serializer.is_valid():

            tax_return_serializer.save(company=company)
            return Response({'message': 'Tax Return created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(tax_return_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_tax_return(request, pk, tr_pk):
    company = get_object_or_404(Company, id=pk)
    tax_return = get_object_or_404(IncomeTaxReturn, id=tr_pk)
    tax_return_serializer = TaxReturnSerializer(data=request.data, instance=tax_return)

    if request.method == "POST":
        if tax_return_serializer.is_valid():
        
            tax_return_serializer.save(company=company)
            return Response({'message': 'Tax Return updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(tax_return_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        tax_return_serializer1=TaxReturnSerializer(tax_return)
    return Response(tax_return_serializer1.data)

@api_view(['DELETE'])
def delete_tax_return(request, pk, tr_pk):
    company = get_object_or_404(Company, id=pk)
    tax_return = get_object_or_404(IncomeTaxReturn, id=tr_pk)
    tax_return.delete()
    return Response({"message": "Tax Return deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST'])
# def create_sales_credit(request,branch_pk,sales_pk):
#     branch = get_object_or_404(Branch, id=branch_pk)
#     sales = get_object_or_404(SalesInvoice, id=sales_pk)
#     if request.method=="POST":
#         credit_serializer = CreditNoteSerializer(data=request.data)
#         if sales_serializer.is_valid():

#             sales_serializer.save(branch=branch)
#             return Response({'message': 'Sales Invoice created successfully.'}, status=status.HTTP_201_CREATED)

#         return Response(sales_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)



# //////////////////sales invoice company///////////////////////

# @api_view(['POST','GET'])
# def create_sales_invoice(request, branch_pk):
#     branch = get_object_or_404(Branch, id=branch_pk)

#     company= branch.company
#     # branch_gst = GstSerializer.objects.filter(branch=branch)
#     if request.method=="GET":
#         # branch_v_serializer = VBranchSerializer(data=request.data)
#         # mn = 
#         gst_no=request.GET.get('mn')
       
#         print("gst_no 123:",gst_no)
#         party_gst = VendorBranch.objects.filter(vendor__company=company,gst=gst_no).first() or ClientVendor.objects.filter(company=company,pan=gst_no).first()

#         if party_gst:
#             if hasattr(party_gst, 'gst'):
#                 # GST field exists in party_gst (VendorBranch)
#                 vendor1 = party_gst.vendor
#                 vendor2 = party_gst
                 
                
#                 # print("branch gst no:",branch_gst)
#                 # if party_gst[0:2] == branch_gst.gst_number[0:2]:
#                 #     branch_gst1 = GstSerializer()
#                 # print("vvvvnnn",vendor2)
#                 branch_gst = Gst.objects.filter(branch=branch)
#                 print("party wala:",branch_gst)
#                 v_branch = VendorSerializer(vendor1)
#                 v_branch1 = VBranchSerializer(vendor2)
#                 branch_gst1 = GstSerializer(branch_gst,many=True)
#                 print("branch gst:",branch_gst1)
#                 combined_data = {
#                 'v_branch': v_branch.data,
#                 'v_branch1': v_branch1.data,
#                 'branch_gst1':branch_gst1.data
#                 }
#                 # print("v branch 1 ka :",v_branch1)
#                 print("v branch sirf ka :",combined_data)
#                 return Response(combined_data)
#             elif hasattr(party_gst, 'pan'):
#                 # Pan field exists in party_gst (ClientVendor)
#                 vendor2 = party_gst
#                 vendor4=party_gst
                
#                 v_branch = VendorSerializer(vendor2)
#                 v_branch3 = VendorSerializer(vendor4)
#                 combined_data={
#                     'v_branch': v_branch.data,
#                     'v_branch3': v_branch3.data,
#                 }
#                 print("vendor 2 pan ka:",combined_data)
#                 return Response(combined_data)
#             else:
#                 return Response({'error_message': "Invalid data"})
#         else:
#             return Response({'error_message': "No vendor found"})
        
#     if request.method == 'POST':
#         # Deserialize the Purchase Invoice data
#         sales_serializer = SalesInvoiceSerializer(data=request.data)

#         if sales_serializer.is_valid():
#             print("total 123 invoie:",request.data)
#             sales_instance = sales_serializer.save(branch=branch)

#             # Extract and prepare product data
#             # print("requet:",request.data)
#             products = []

#             for key, value in request.data.items():
#                 if key.startswith('products'):
#                     parts = key.split('[')
                    
#                     product_index = int(parts[1][:-1])  # Extract the index from the key without the trailing ']'
#                     product_key = parts[2][:-1]  # Extract the inner key without the trailing ']'
#                     if len(products) < product_index + 1:
#                         products.append({})  # Ensure the products list has space for the current index

#                     products[product_index][product_key] = value  # Assign the inner key-value pair to the appropriate product
#             print("sales_serializer",sales_serializer)
#             for index, product_dict in enumerate(products, start=0):
#                 product1 = ProductSales.objects.create(
                
#                 sales_invoice=sales_instance,
#                 hsn=product_dict.get('hsn', 'No hsn'),
#                 product_name = product_dict.get('product_name', 'No Product'),
#                 unit_of_measure=product_dict.get('unit_of_measure', 'No measure'),
#                 unit=product_dict.get('unit', 'No unit'),
#                 rate=product_dict.get('rate', 'No rate'),
#                 gst_per=product_dict.get('gst_per', 'No gst_per'),
#                 cgst=product_dict.get('cgst', 'No cgst'),
#                 sgst=product_dict.get('sgst', 'No sgst'),
#                 taxable_amount=product_dict.get('taxable_amount', 'No amount_receivable'),
    
#             )


#             return Response({'message': 'Sales Invoice created successfully.', 'id': sales_instance.id}, status=status.HTTP_201_CREATED)

#         # Handle validation errors for Purchase Invoice
#         return Response({'error': sales_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST','GET'])
def create_sales_invoice_company(request,pk):
    company = get_object_or_404(Company, id=pk)

    # company= branch.company
    # branch_gst = GstSerializer.objects.filter(branch=branch)
    if request.method=="GET":
        # branch_v_serializer = VBranchSerializer(data=request.data)
        # mn = 
        gst_no=request.GET.get('mn')
        branch_id = request.GET.get('branch_id')

       
        print("gst_no 123:",gst_no)
        party_gst = VendorBranch.objects.filter(vendor__company=company,gst=gst_no).first() or ClientVendor.objects.filter(company=company,pan=gst_no).first()

        if party_gst:
            if hasattr(party_gst, 'gst'):
                # GST field exists in party_gst (VendorBranch)
                vendor1 = party_gst.vendor
                vendor2 = party_gst
                 
                
            
                branch_gst = Gst.objects.filter(branch=branch_id)
                print("party wala:",branch_gst)
                v_branch = VendorSerializer(vendor1)
                v_branch1 = VBranchSerializer(vendor2)
                branch_gst1 = GstSerializer(branch_gst,many=True)
                print("branch gst:",branch_gst1)
                combined_data = {
                'v_branch': v_branch.data,
                'v_branch1': v_branch1.data,
                'branch_gst1':branch_gst1.data
                }
                # print("v branch 1 ka :",v_branch1)
                print("v branch sirf ka :",combined_data)
                return Response(combined_data)
            elif hasattr(party_gst, 'pan'):
                # Pan field exists in party_gst (ClientVendor)
                vendor2 = party_gst
                vendor4=party_gst
                
                v_branch = VendorSerializer(vendor2)
                v_branch3 = VendorSerializer(vendor4)
                combined_data={
                    'v_branch': v_branch.data,
                    'v_branch3': v_branch3.data,
                }
                print("vendor 2 pan ka:",combined_data)
                return Response(combined_data)
            else:
                return Response({'error_message': "Invalid data"})
        else:
            return Response({'error_message': "No vendor found"})
        
    if request.method == 'POST':
        # Deserialize the Purchase Invoice data
        sales_serializer = SalesCompanySerializer(data=request.data)

        if sales_serializer.is_valid():
            print("total 123 invoie:",request.data)
            branch = sales_serializer.validated_data.get('branch')

            sales_instance = sales_serializer.save(branch=branch)

            # Extract and prepare product data
            # print("requet:",request.data)
            products = []

            for key, value in request.data.items():
                if key.startswith('products'):
                    parts = key.split('[')
                    
                    product_index = int(parts[1][:-1])  # Extract the index from the key without the trailing ']'
                    product_key = parts[2][:-1]  # Extract the inner key without the trailing ']'
                    if len(products) < product_index + 1:
                        products.append({})  # Ensure the products list has space for the current index

                    products[product_index][product_key] = value  # Assign the inner key-value pair to the appropriate product
            print("sales_serializer",sales_serializer)
            for index, product_dict in enumerate(products, start=0):
                product1 = ProductSales.objects.create(
                
                sales_invoice=sales_instance,
                hsn=product_dict.get('hsn', 'No hsn'),
                product_name = product_dict.get('product_name', 'No Product'),
                unit_of_measure=product_dict.get('unit_of_measure', 'No measure'),
                unit=product_dict.get('unit', 'No unit'),
                rate=product_dict.get('rate', 'No rate'),
                gst_per=product_dict.get('gst_per', 'No gst_per'),
                cgst=product_dict.get('cgst', '0'),
                sgst=product_dict.get('sgst', '0'),
                igst=product_dict.get('igst', '0'),
                taxable_amount=product_dict.get('taxable_amount', '0')
                # cgst=product_dict.get('cgst', 'No cgst'),
                # sgst=product_dict.get('sgst', 'No sgst'),
                # taxable_amount=product_dict.get('taxable_amount', 'No amount_receivable'),
    
            )


            return Response({'message': 'Sales Invoice created successfully.', 'id': sales_instance.id}, status=status.HTTP_201_CREATED)

        # Handle validation errors for Purchase Invoice
        return Response({'error': sales_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




# credit note company

@api_view(['POST','GET'])
def create_credit_note_company(request, branch_pk,sales_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    sales = get_object_or_404(SalesInvoice, id=sales_pk)
    company =branch.company
    # print("abc22:",abc)
    # branch_gst = GstSerializer.objects.filter(branch=branch)
    if request.method=="GET":
        # branch_v_serializer = VBranchSerializer(data=request.data)
        # mn = 
        gst_no=request.GET.get('mn')
       
        print("gst_no 123:",gst_no)
        party_gst = VendorBranch.objects.filter(vendor__company=company,gst=gst_no).first() or ClientVendor.objects.filter(company=company,pan=gst_no).first()

        if party_gst:
            if hasattr(party_gst, 'gst'):
                # GST field exists in party_gst (VendorBranch)
                vendor1 = party_gst.vendor
                vendor2 = party_gst
                 
                
                # print("branch gst no:",branch_gst)
                # if party_gst[0:2] == branch_gst.gst_number[0:2]:
                #     branch_gst1 = GstSerializer()
                # print("vvvvnnn",vendor2)
                branch_gst = Gst.objects.filter(branch=branch)
                print("party wala:",branch_gst)
                v_branch = VendorSerializer(vendor1)
                v_branch1 = VBranchSerializer(vendor2)
                branch_gst1 = GstSerializer(branch_gst,many=True)
                print("branch gst:",branch_gst1)
                combined_data = {
                'v_branch': v_branch.data,
                'v_branch1': v_branch1.data,
                'branch_gst1':branch_gst1.data
                }
                # print("v branch 1 ka :",v_branch1)
                print("v branch sirf ka :",combined_data)
                return Response(combined_data)
            elif hasattr(party_gst, 'pan'):
                # Pan field exists in party_gst (ClientVendor)
                vendor2 = party_gst
                vendor4=party_gst
                
                v_branch = VendorSerializer(vendor2)
                v_branch3 = VendorSerializer(vendor4)
                combined_data={
                    'v_branch': v_branch.data,
                    'v_branch3': v_branch3.data,
                }
                print("vendor 2 pan ka:",combined_data)
                return Response(combined_data)
            else:
                return Response({'error_message': "Invalid data"})
        else:
            return Response({'error_message': "No vendor found"})
        
    if request.method == 'POST':
        # Deserialize the Purchase Invoice data
        sales_serializer = CreditNoteSerializer(data=request.data)

        if sales_serializer.is_valid():
            print("total invoie:",request.data)
            sales_instance = sales_serializer.save(branch=branch, sales_invoice=sales)
            print("pbb",sales_instance)
            # Extract and prepare product data
            # print("requet:",request.data)
            products = []

            for key, value in request.data.items():
                if key.startswith('products'):
                    parts = key.split('[')
                    
                    product_index = int(parts[1][:-1])  # Extract the index from the key without the trailing ']'
                    product_key = parts[2][:-1]  # Extract the inner key without the trailing ']'
                    if len(products) < product_index + 1:
                        products.append({})  # Ensure the products list has space for the current index

                    products[product_index][product_key] = value  # Assign the inner key-value pair to the appropriate product

            # print(products)
            # products2 = list(products)
            # Create ProductDetails instances linked to the PurchaseInvoice
            # print("products 2:",products2)
            # for i in products:
            # for product in products:
            #     for key, value, index in product.items():
            #         print(f"Key: {key}, Value: {value}, index:{index}")
            for index, product_dict in enumerate(products, start=0):
                product1 = CreditProduct.objects.create(
                
                credit_note=sales_instance,
                # hsn=products[i].get('hsn') if products[0].get('hsn') else 'No HSN',
                hsn=product_dict.get('hsn', 'No hsn'),
                # product_name="watches",
                product_name = product_dict.get('product_name', 'No Product'),
                unit_of_measure=product_dict.get('unit_of_measure', 'No measure'),
                unit=product_dict.get('unit', 'No unit'),
                rate=product_dict.get('rate', 'No rate'),
                gst_per=product_dict.get('gst_per', 'No gst_per'),
                # cgst=product_dict.get('cgst', 'No cgst'),
                # hsn="24",
                # product_name=products[i].get('product_name') if products[i].get('product_name') else 'No Product',
                # unit_of_measure=products[i].get('unit_of_measure') if products[i].get('unit_of_measure') else 'No unit of measure',
                # ... other fields
            )

            # Calculate and update total_invoice field in Purchase Invoice
            # purchase_instance.calculate_total_invoice()

            return Response({'message': 'Purchase Invoice created successfully.', 'id': sales_instance.id}, status=status.HTTP_201_CREATED)

        # Handle validation errors for Purchase Invoice
        return Response({'error': sales_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def purchase_detail(request,pk,purchase_pk):
    branch = Branch.objects.get(id=pk)
    purchase_detail = PurchaseInvoice.objects.get(id=purchase_pk,branch=branch)
    product_detail = ProductDetails.objects.filter(purchase_invoice=purchase_detail)
    
    print("3333",product_detail,"2222",purchase_detail,"11111",branch)
    p_serializer = PurchaseCompanySerializer(purchase_detail)
    vendor_data = p_serializer.data['gst_no']
    vendor_detail = VendorBranch.objects.get(gst=vendor_data)
    produc_serializer = ProductDetailsSerializer(product_detail,many=True)
    print("444444",produc_serializer)
    vendor_serializer = VBranchSerializer(vendor_detail)

    data={
        "purchase": p_serializer.data,
        "product": produc_serializer.data,
        "adress":vendor_serializer.data['address'],
    }
    print("kkkkkkkkkkkk",data)
    return Response(data)
    # print(purchase_detail)


@api_view(['GET'])
def sales_detail(request,pk,sales_pk):
    branch = Branch.objects.get(id=pk)
    sales_detail = SalesInvoice.objects.get(id=sales_pk,branch=branch)
    product_detail = ProductSales.objects.filter(sales_invoice=sales_detail)
    
    print("3333",product_detail,"2222",purchase_detail,"11111",branch)
    s_serializer = SalesCompanySerializer(sales_detail)
    vendor_data = s_serializer.data['gst_no']
    vendor_detail = VendorBranch.objects.get(gst=vendor_data)
    produc_serializer = ProductSalesSerializer(product_detail,many=True)
    print("444444",produc_serializer)
    vendor_serializer = VBranchSerializer(vendor_detail)

    data={
        "sales": s_serializer.data,
        "product": produc_serializer.data,
        "adress":vendor_serializer.data['address'],
    }
    print("kkkkkkkkkkkk",data)
    return Response(data)
# ProductSalesSerializer    # print(purchase_detail)


@api_view(['GET'])
def debit_detail(request,pk,debit_pk):
    purchase = PurchaseInvoice.objects.get(id=pk)
    debit_detail = DebitNote.objects.get(id=debit_pk,purchase_invoice=purchase)
    product_detail = DebitProduct.objects.filter(debit_note=debit_detail)
    
    # print("3333",product_detail,"2222",purchase_detail,"11111",branch)
    d_serializer = DebitNoteSerializer(debit_detail)
    vendor_data = d_serializer.data['gst_no']
    vendor_detail = VendorBranch.objects.get(gst=vendor_data)
    produc_serializer = DebitProductSerializer(product_detail,many=True)
    print("444444",produc_serializer)
    vendor_serializer = VBranchSerializer(vendor_detail)

    data={
        "debit": d_serializer.data,
        "product": produc_serializer.data,
        "adress":vendor_serializer.data['address'],
    }
    print("kkkkkkkkkkkk",data)
    return Response(data)
    # print(purchase_detail)
    
    
@api_view(['GET'])
def credit_detail(request,pk,credit_pk):
    sales = SalesInvoice.objects.get(id=pk)
    credit_detail = CreditNote.objects.get(id=credit_pk,sales_invoice=sales)
    product_detail = CreditProduct.objects.filter(credit_note=credit_detail)
    
    # print("3333",product_detail,"2222",purchase_detail,"11111",branch)
    c_serializer = CreditNoteSerializer(credit_detail)
    vendor_data = c_serializer.data['gst_no']
    vendor_detail = VendorBranch.objects.get(gst=vendor_data)
    produc_serializer = CreditProductSerializer(product_detail,many=True)
    print("444444",produc_serializer)
    vendor_serializer = VBranchSerializer(vendor_detail)

    data={
        "credit": c_serializer.data,
        "product": produc_serializer.data,
        "adress":vendor_serializer.data['address'],
    }
    print("kkkkkkkkkkkk",data)
    return Response(data)
    # print(purchase_detail)
    
    
    
@api_view(['POST'])
@parser_classes([MultiPartParser])
def create_financial_year(request, pk):
    company = get_object_or_404(Company, id=pk)

    if request.method == "POST":
        # Get files from the request
        computation_files = request.FILES.getlist('computation')
        acknowledgement_files = request.FILES.getlist('acknowledgement')

        # Remove file fields from data
        data = request.data.copy()
        data.pop('computation', None)
        data.pop('acknowledgement', None)

        financial_serializer = FinancialYearSerializer(data=data)
        
        if financial_serializer.is_valid():
            financial_instance = financial_serializer.save(company=company)

            # Save computation files
            for file in computation_files:
                ComputationFile.objects.create(file=file, financial_year=financial_instance)

            # Save acknowledgement files
            for file in acknowledgement_files:
                AcknowledgementFile.objects.create(file=file, financial_year=financial_instance)

            return Response({'message': 'Financial Serializer created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(financial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




@api_view(['POST'])
@parser_classes([MultiPartParser])
def create_financial2_year(request):
    if request.method == "POST":
        financial_serializer = Financial2YearSerializer(data=request.data)

        if financial_serializer.is_valid():
            # Access the computation and acknowledgement files data from request.data
            computation_files_data = request.data
            print('computation_files_data',computation_files_data)

            # Create a Financial2Year instance with other fields from serializer
            financial_instance = financial_serializer.save()

            # Save computation files
            for computation_file_data in computation_files_data:
                computation_instance = ComputationFile.objects.create(
                    file=computation_file_data,
                    financial_instance=financial_instance
                )
                # Customize the above line based on your model structure

            # Save acknowledgement files
            # for acknowledgement_file_data in acknowledgement_files_data:
            #     acknowledgement_instance = AcknowledgementFile.objects.create(
            #         file=acknowledgement_file_data,
            #         financial_instance=financial_instance
            #     )
                # Customize the above line based on your model structure

            return Response({'message': 'Files processed successfully'}, status=status.HTTP_201_CREATED)

        return Response(financial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




# @api_view(['POST'])
# @parser_classes([MultiPartParser])
# def create_financial_year(request, pk):
#     company = get_object_or_404(Company, id=pk)

#     if request.method == "POST":
#         acknowledgement_files = request.FILES.getlist('acknowledgement_files')
#         computation_files = request.FILES.getlist('computation_files')

#         # Extract only the fields needed for FinancialYearSerializer
#         data = {
#             'field1': request.data.get('field1'),
#             'field2': request.data.get('field2'),
#             # Add other fields as needed
#         }

#         financial_serializer = FinancialYearSerializer(data=data)
        
#         if financial_serializer.is_valid():
#             financial_instance = financial_serializer.save(company=company)

#             # Handle bulk upload for acknowledgement_files
#             for file in acknowledgement_files:
#                 financial_instance.acknowledgement.create(file=file)

#             # Handle bulk upload for computation_files
#             for file in computation_files:
#                 financial_instance.computation.create(file=file)

#             return Response({'message': 'Financial Serializer created successfully.'}, status=status.HTTP_201_CREATED)

#         return Response(financial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def financial_update(request,pk,financial_pk):
    company = get_object_or_404(Company, id=pk)
    financial_year = get_object_or_404(FinancialYear, id=financial_pk)
    financial_serializer = FinancialYearSerializer(data=request.data, instance=financial_year)

    if request.method=="POST":
        if financial_serializer.is_valid():
           
            financial_serializer.save(company=company)
            return Response({'message':'Financial Year updated successfully!'},status=status.HTTP_200_OK)
        return Response(financial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='GET':
        # return Response(owner_serializer.initial_data,{'message':"working"})
        financial_serializer_1 = FinancialYearSerializer(financial_year)
        return Response(financial_serializer_1.data)


@api_view(['DELETE'])
def financial_delete(request,pk):
    Financial_year = FinancialYear.objects.get(id=pk)
    Financial_year.delete()
    return Response({"message": "Financial Year deleted successfully"}, status=status.HTTP_204_NO_CONTENT)






# class YourModelCreateView(generics.CreateAPIView):
#     queryset = YourModel.objects.all()
#     serializer_class = YourModelSerializer

#     def create(self, request, *args, **kwargs):
#         # Extract 'computation' and 'acknowledgement' files
#         computation_files = request.FILES.getlist('computation')
#         acknowledgement_files = request.FILES.getlist('acknowledgement')

#         # Extract other fields from request.data
#         date = request.data.get('date')

#         # Create the main model instance with other fields
#         instance = YourModel.objects.create(date=date)

#         # Associate 'computation' files with the instance
#         for computation_file in computation_files:
#             instance.computation.create(file=computation_file)

#         # Associate 'acknowledgement' files with the instance
#         for acknowledgement_file in acknowledgement_files:
#             instance.acknowledgement.create(file=acknowledgement_file)

#         # Return a response
#         serializer = YourModelSerializer(instance)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)



class YourModelCreateView(generics.CreateAPIView):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer

    def create(self, request, *args, **kwargs):
        # Extract 'computation' and 'acknowledgement' files
        computation_files = request.FILES.getlist('computation')
        acknowledgement_files = request.FILES.getlist('acknowledgement')

        # Extract other fields from request.data
        return_type = request.data.get('return_type')
        from_date = request.data.get('from_date')
        to_date = request.data.get('to_date')
        month = request.data.get('month')
        frequency = request.data.get('frequency')
        client_review = request.data.get('client_review')
        remark = request.data.get('remark')
        company_id = kwargs.get('company_id')
        print("from_date",from_date)
        try:
            # Get the Company instance based on the provided ID
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return Response({"message": "Company not found"}, status=status.HTTP_404_NOT_FOUND)

        # Create the main model instance with other fields
        instance = YourModel.objects.create(
            return_type=return_type,
            from_date=from_date,
            to_date=to_date,
            month=month,
            frequency=frequency,
            client_review=client_review,
            remark=remark,
            company=company
        )

        # Associate 'computation' files with the instance
        for computation_file in computation_files:
            instance.computation.create(file=computation_file)

        # Associate 'acknowledgement' files with the instance
        for acknowledgement_file in acknowledgement_files:
            instance.acknowledgement.create(file=acknowledgement_file)

        # Return a response
        serializer = YourModelSerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['POST','GET'])
# def financial_update(request,pk,financial_pk):
#     company = get_object_or_404(Company, id=pk)
#     financial_year = get_object_or_404(FinancialYear, id=financial_pk)
#     financial_serializer = FinancialYearSerializer(data=request.data, instance=financial_year)

#     if request.method=="POST":
#         if financial_serializer.is_valid():
           
#             financial_serializer.save(company=company)
#             return Response({'message':'Financial Year updated successfully!'},status=status.HTTP_200_OK)
#         return Response(financial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method=='GET':
#         # return Response(owner_serializer.initial_data,{'message':"working"})
#         financial_serializer_1 = FinancialYearSerializer(financial_year)
#         return Response(financial_serializer_1.data)

class YourModelUpdateView(RetrieveUpdateAPIView):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer

    def retrieve(self, request, *args, **kwargs):
        # Handle GET request to retrieve data for editing
        instance = self.get_object()
        serializer = YourModelSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        # Handle PATCH request to update data
        # Extract 'computation' and 'acknowledgement' files
        computation_files = request.FILES.getlist('computation')
        acknowledgement_files = request.FILES.getlist('acknowledgement')

        # Get the existing instance to update
        instance = self.get_object()

        # Use the serializer to handle data validation and conversion
        serializer = YourModelSerializer(instance, data=request.data, partial=True)
        
        if serializer.is_valid():
            # Save the changes
            serializer.save()

            # Associate 'computation' files with the instance
            for computation_file in computation_files:
                instance.computation.create(file=computation_file)

            # Associate 'acknowledgement' files with the instance
            for acknowledgement_file in acknowledgement_files:
                instance.acknowledgement.create(file=acknowledgement_file)

            # Return a response
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
def report_detail(request,pk):
    report = YourModel.objects.get(id=pk)
    computation = ComputationFileModel.objects.filter(your_model=report)
    # branch = purchase_invoice.branch
    print('computation',computation)
    # filter ends here
    
    computation_serializer = ComputationFileModelSerializer(computation,many=True)
    

  
       

    data = {
        "computation_serializer": computation_serializer.data,
    
    }
    return Response(data)





