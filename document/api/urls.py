
from django.urls import path
from api import views

urlpatterns = [
    path('', views.Home,name="home"),
    #Company Urls
    path('create-company', views.create_company,name="create-company"),
    path('company-list', views.company_list,name="company-list"),
    path('company-update/<int:pk>', views.company_update,name="company-update"),
    path('company-api/<int:pk>', views.company_api,name="company-api"),
    path('company-delete/<int:pk>', views.company_delete,name="company-delete"),

    # company details
    path('company-details/<int:pk>', views.company_details,name="company-details"),

    #User Urls
    path('create-user/<int:company_id>', views.create_user,name="create-user"),
    path('user-update/<int:pk>', views.user_update,name="user-update"),
    #Branch Urls
    path('create-branch/<int:pk>', views.create_branch,name="create-branch"),
    path('update-branch/<int:pk>/<int:branch_pk>', views.update_branch,name="update-branch"),
    path('delete-branch/<int:pk>/<int:branch_pk>', views.update_branch,name="delete-branch"),
    #Owner Urls
    path('create-owner/<int:pk>', views.create_owner,name="create-owner"),
    path('update-owner/<int:pk>/<int:owner_pk>', views.update_owner,name="update-owner"),
    path('delete-owner/<int:pk>/<int:owner_pk>', views.delete_owner,name="delete-owner"),
    #Bank urls
    path('create-bank/<int:pk>', views.create_bank_details,name="create-bank"),
    path('update-bank/<int:pk>/<int:bank_pk>', views.update_bank,name="update-bank"),
    path('delete-bank/<int:pk>/<int:bank_pk>', views.delete_owner,name="delete-owner"),
    #Aadhar urls
    path('create-aadhar/<int:pk>', views.create_aadhar,name="create-aadhar"),
    path('update-aadhar/<int:pk>/<int:aadhar_pk>', views.update_aadhar,name="update-aadhar"),
    path('delete-aadhar/<int:pk>/<int:aadhar_pk>', views.delete_aadhar,name="delete-aadhar"),


    # path('notes/<int:pk>', views.get_single_note,name="notes"),
    
]







