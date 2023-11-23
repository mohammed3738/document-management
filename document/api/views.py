from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import*
from .serializers import *
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from .forms import *
from rest_framework import status


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


# company create view


@api_view(['POST'])
def create_company(request):
    if request.method == "POST":
        company_serializer = CompanySerializer(data=request.data)

        if company_serializer.is_valid():
            company_serializer.save()
            return Response({"message": "Company created successfully"}, status=status.HTTP_201_CREATED)

        return Response({"message:not created"},company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def company_list(request):
    company_lists=Company.objects.all()
    serializer=CompanySerializer(company_lists,many=True)
    
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
    # print(owner_serializer.id)
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
        "tax":tax_serializer.data
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



# ************sales invoice views***************


@api_view(['POST'])
def create_sales_invoice(request,branch_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    if request.method=="POST":
        sales_serializer = SalesInvoiceSerializer(data=request.data)
        
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

    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


# @api_view(['POST'])
# def create_sales_invoice(request,branch_pk):
#     branch = get_object_or_404(Branch, id=branch_pk)
#     if request.method=="POST":
#         sales_serializer = SalesInvoiceSerializer(data=request.data)
#         if sales_serializer.is_valid():

#             sales_serializer.save(branch=branch)
#             return Response({'message': 'Sales Invoice created successfully.'}, status=status.HTTP_201_CREATED)

#         return Response(sales_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)



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

@api_view(['POST'])
def create_credit_note(request,branch_pk,sales_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    sales = get_object_or_404(SalesInvoice, id=sales_pk)
    if request.method=="POST":
        credit_note_serializer = CreditNoteSerializer(data=request.data)
        if credit_note_serializer.is_valid():

            credit_note_serializer.save(branch=branch,sales_in=sales)
            return Response({'message': 'Credit Note created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(credit_note_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


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
    cr_note = CreditNote.objects.filter(branch=branch,sales_in=sales)

    # print(owner_serializer.id)
    cr_note_serializer = CreditNoteSerializer(cr_note,many=True)


    data = {
        "credit": cr_note_serializer.data,
  
    }
    return Response(data)

# *************purchase invoice views*************
@api_view(['POST'])
def create_purchase_invoice(request, branch_pk):
    branch = get_object_or_404(Branch, id=branch_pk)

    if request.method == 'POST':
        purchase_serializer = PurchaseInvoiceSerializer(data=request.data)

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

    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

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
@api_view(['POST'])
def create_debit_note(request,branch_pk,purchase_pk):
    branch = get_object_or_404(Branch, id=branch_pk)
    purchase = get_object_or_404(PurchaseInvoice, id=purchase_pk)
    if request.method=="POST":
        debit_note_serializer = DebitNoteSerializer(data=request.data)
        if debit_note_serializer.is_valid():

            debit_note_serializer.save(branch=branch,purchase_in=purchase)
            return Response({'message': 'Debit Note created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(debit_note_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


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
    db_note = DebitNote.objects.filter(branch=branch,purchase_in=purchase)

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


