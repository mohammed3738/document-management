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
    # print(owner_serializer.id)
    owner_serializer = OwnerSerializer(owner_list,many=True)
    branch_serializer = BranchSerializer(branch_list,many=True)
    user_serializer = UserSerializer(user_list,many=True)

    data = {
        "owners": owner_serializer.data,
        "branches": branch_serializer.data,
        "users":user_serializer.data
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
    bank_serializer = BankSerializer(dat=request.data, instance=bank)

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
        aadhar_serializer = AadharSerializer(request.data)
        if aadhar_serializer.is_valid():
         
            aadhar_serializer.save(company=company)
            return Response({'message': 'Udhyam Aadhar created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(aadhar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def update_aadhar(request, pk, aadhar_pk):
    company = get_object_or_404(Company, id=pk)
    aadhar = get_object_or_404(UdyamAadhar, id=aadhar_pk)

    if request.method == "POST":
        aadhar_serializer = AadharSerializer(request.data, instance=aadhar)
        if aadhar_serializer.is_valid():
        
            aadhar_serializer.save(company=company)
            return Response({'message': 'Udhyam Aadhar updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(aadhar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
        tan_serializer = TanSerializer(request.data)
        if tan_serializer.is_valid():

            tan_serializer.save(company=company)
            return Response({'message': 'Tan created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(tan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_tan(request, pk, tan_pk):
    company = get_object_or_404(Company, id=pk)
    tan = get_object_or_404(Tan, id=tan_pk)
    tan_serializer = TanSerializer(request.data, instance=tan)

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
        ptrc_serializer = PtrcSerializer(request.data)
        if ptrc_serializer.is_valid():

            ptrc_serializer.save(company=company)
            return Response({'message': 'Ptrc created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(ptrc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_ptrc(request, pk, ptrc_pk):
    company = get_object_or_404(Company, id=pk)
    ptrc = get_object_or_404(Ptrc, id=ptrc_pk)
    ptrc_serializer = PtrcSerializer(request.data, instance=ptrc)

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
        ptec_serializer = PtecSerializer(request.data)
        if ptec_serializer.is_valid():

            ptec_serializer.save(company=company)
            return Response({'message': 'Ptec created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(ptec_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST','GET'])
def update_ptec(request, pk, ptec_pk):
    company = get_object_or_404(Company, id=pk)
    ptec = get_object_or_404(Ptec, id=ptec_pk)
    ptec_serializer = PtecSerializer(request.data, instance=ptec)

    if request.method == "POST":
        if ptec_serializer.is_valid():
        
            ptec_serializer.save(company=company)
            return Response({'message': 'Ptrc updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(ptec_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="GET":
        ptec_serializer1=PtrcSerializer(ptec)
    return Response(ptec_serializer1.data)


@api_view(['DELETE'])
def delete_ptec(request, pk, ptec_pk):
    company = get_object_or_404(Company, id=pk)
    ptec = get_object_or_404(Ptec, id=ptec_pk)
    ptec.delete()
    return Response({"message": "Ptec deleted successfully"}, status=status.HTTP_204_NO_CONTENT)