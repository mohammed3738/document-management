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


@api_view(['POST'])
def company_update(request, pk):
    company = Company.objects.get(id=pk)
    if request.method=="POST":
        company_serializer = CompanySerializer(instance=company, data=request.data)
        if company_serializer.is_valid():
            company_serializer.save()
            return Response({'message':'Company updated successfully!'},status=status.HTTP_200_OK)
        return Response(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


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
        user_serializer = UserSerializer(data=request.data)  # Use UserSerializer to validate the data
        if user_serializer.is_valid():
            user_serializer.save(company=company)  # Save the user with the associated company

            # Extract email and username from the validated data
            user_email = user_serializer.validated_data.get('email')
            username = user_serializer.validated_data.get('username')
            password = user_serializer.validated_data.get('password1')

            # Prepare email content
            subject = "User Credentials"
            message = f"Your login credentials:\nUsername: {username}\nPassword: {password}"
            from_email = "mmbaig461@gmail.com"
            recipient_list = [user_email]

            # Send email
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return Response({'message':'Created User Successfully'},status=status.HTTP_201_CREATED)

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


@api_view(['POST'])
def update_branch(request,pk, branch_pk):
    company = get_object_or_404(Company, id=pk)
    branch = get_object_or_404(Branch, id=branch_pk)

    if request.method=="POST":
        branch_serializer = BranchSerializer(data=request.data, instance=branch)
        if branch_serializer.is_valid():
           
            branch_serializer.save(company=company)
            return Response({'message':'Branch updated successfully!'},status=status.HTTP_200_OK)
        return Response(branch_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['DELETE'])
def branch_delete(request,pk,branch_pk):
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


@api_view(['POST'])
def update_owner(request, pk, owner_id):
    company = get_object_or_404(Company, id=pk)
    owner = get_object_or_404(OwnerDetails, id=owner_id)
    if request.method=="POST":
        owner_serializer = OwnerSerializer(data=request.data,instance=owner)
        if owner_serializer.is_valid():
            owner_serializer.save(company=company)
            return Response({'message': 'Owner updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(owner_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def delete_owner(request,pk,owner_id):
    company = get_object_or_404(Company, id=pk)
    owner = get_object_or_404(OwnerDetails, id=owner_id)
    owner.delete()
    return Response({"message": "Owner deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# ******************** bank details views********************

@api_view(['POST'])
def create_bank_details(request,pk):
    company = get_object_or_404(Company,id=pk)
    if request.method=="POST":
        bank_serializer = BankSerializer(request.data)
        if bank_serializer.is_valid():
         
            bank_serializer.save(company=company)
            return Response({'message': 'Bank Details created successfully.'}, status=status.HTTP_201_CREATED)

        return Response(bank_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def update_bank(request,pk,bank_id):
    company = get_object_or_404(Company, id=pk)
    bank = get_object_or_404(BankDetails, id=bank_id)
    if request.method=="POST":
        bank_serializer = BankSerializer(request.data,instance=bank)
        if bank_serializer.is_valid():
           
            bank_serializer.save(company=company)
            return Response({'message': 'Bank updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(bank_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)




@api_view(['DELETE'])
def delete_bank(request,pk,bank_id):
    company = get_object_or_404(Company, id=pk)
    bank = get_object_or_404(BankDetails, id=bank_id)
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
def update_aadhar(request, pk, aadhar_id):
    company = get_object_or_404(Company, id=pk)
    aadhar = get_object_or_404(UdyamAadhar, id=aadhar_id)

    if request.method == "POST":
        aadhar_serializer = AadharSerializer(request.data, instance=aadhar)
        if aadhar_serializer.is_valid():
        
            aadhar_serializer.save(company=company)
            return Response({'message': 'Udhyam Aadhar updated successfully.'}, status=status.HTTP_201_CREATED)
        return Response(aadhar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Method not allowed'},status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def delete_aadhar(request, pk, aadhar_id):
    company = get_object_or_404(Company, id=pk)
    aadhar = get_object_or_404(UdyamAadhar, id=aadhar_id)
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

