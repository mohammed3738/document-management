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

        return Response(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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









#   view_user = CustomUser.objects.all()
#     user_serializer = UserSerializer(view_user, many=True)


# @api_view(['GET'])
# def get_notes(request):
#     companies = Company.objects.all()
#     serializers = CompanySerializer(companies, many=True)
#     return Response(serializers.data)



# @api_view(['GET'])
# def get_single_note(request,pk):
#     companies = Company.objects.get(id=pk)
#     serializers = CompanySerializer(companies, many=False)
#     return Response(serializers.data)