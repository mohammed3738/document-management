
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import*
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.



@api_view(['POST'])
def create_vendor(request,pk):
    company = get_object_or_404(Company,id=pk)

    if request.method == "POST":
        vendor_serializer = VendorSerializer(data=request.data)

        if vendor_serializer.is_valid():
            vendor_serializer.save(company=company)
            return Response({"message": "Vendor created successfully"}, status=status.HTTP_201_CREATED)

        return Response({"message:not created"},vendor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def vendor_details(request,vendor_pk):
    vendor = ClientVendor.objects.get(id=vendor_pk)
    branch_list = VendorBranch.objects.filter(vendor=vendor)

    # print(owner_serializer.id)
    branch_serailizer = VBranchSerializer(branch_list,many=True)
    # purchase_serializer = PurchaseInvoiceSerializer(purchase_list,many=True)
    # sales_serializer = SalesInvoiceSerializer(sales_list,many=True)


    data = {
        "branch": branch_serailizer.data,
     
  
    }
    return Response(data)


# @api_view(['POST'])
# def create_vendor_branch(request,pk):
#     vendor = get_object_or_404(ClientVendor,id=pk)

#     if request.method == "POST":
#         branch_serializer = VBranchSerializer(data=request.data)

#         if branch_serializer.is_valid():
#             branch_serializer.save(vendor=vendor)
#             return Response({"message": "Vendor branch created successfully"}, status=status.HTTP_201_CREATED)

#         return Response({"message:not created"},branch_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['POST'])
def create_vendor_branch(request, pk):
    vendor = get_object_or_404(ClientVendor, id=pk)

    if request.method == "POST":
        branch_serializer = VBranchSerializer(data=request.data)

        if branch_serializer.is_valid():
            branch_serializer.save(vendor=vendor)
            return Response({"message": "Vendor created successfully"}, status=status.HTTP_201_CREATED)

        return Response({"message": "not created", "errors": branch_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)