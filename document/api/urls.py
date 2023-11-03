
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
    path('user-update/<int:pk>/<int:user_pk>', views.user_update,name="user-update"),
    #Branch Urls
    path('create-branch/<int:pk>', views.create_branch,name="create-branch"),
    path('update-branch/<int:pk>/<int:branch_pk>', views.update_branch,name="update-branch"),
    path('delete-branch/<int:pk>/<int:branch_pk>', views.delete_branch,name="delete-branch"),
    #Owner Urls
    path('create-owner/<int:pk>', views.create_owner,name="create-owner"),
    path('update-owner/<int:pk>/<int:owner_pk>', views.update_owner,name="update-owner"),
    path('delete-owner/<int:pk>/<int:owner_pk>', views.delete_owner,name="delete-owner"),
    #Bank urls
    path('create-bank/<int:pk>', views.create_bank_details,name="create-bank"),
    path('update-bank/<int:pk>/<int:bank_pk>', views.update_bank,name="update-bank"),
    path('delete-bank/<int:pk>/<int:bank_pk>', views.delete_bank,name="delete-bank"),
    #Aadhar urls
    path('create-aadhar/<int:pk>', views.create_aadhar,name="create-aadhar"),
    path('update-aadhar/<int:pk>/<int:aadhar_pk>', views.update_aadhar,name="update-aadhar"),
    path('delete-aadhar/<int:pk>/<int:aadhar_pk>', views.delete_aadhar,name="delete-aadhar"),
    # Tan urls
    path('create-tan/<int:pk>', views.create_tan,name="create-tan"),
    path('update-tan/<int:pk>/<int:tan_pk>', views.update_tan,name="update-tan"),
    path('delete-tan/<int:pk>/<int:tan_pk>', views.delete_tan,name="delete-tan"),
    # Ptrc urls
    path('create-ptrc/<int:pk>', views.create_ptrc,name="create-ptrc"),
    path('update-ptrc/<int:pk>/<int:ptrc_pk>', views.update_ptrc,name="update-ptrc"),
    path('delete-ptrc/<int:pk>/<int:ptrc_pk>', views.delete_ptrc,name="delete-ptrc"),
    # Ptec urls
    path('create-ptec/<int:pk>', views.create_ptec,name="create-ptec"),
    path('update-ptec/<int:pk>/<int:ptec_pk>', views.update_ptec,name="update-ptec"),
    path('delete-ptec/<int:pk>/<int:ptec_pk>', views.delete_ptec,name="delete-ptec"),
    # Pan urls
    path('create-pan/<int:pk>', views.create_pan,name="create-pan"),
    path('update-pan/<int:pk>/<int:pan_pk>', views.update_pan,name="update-pan"),
    path('delete-pan/<int:pk>/<int:pan_pk>', views.delete_pan,name="delete-pan"),
    # Msme urls
    path('create-msme/<int:pk>', views.create_msme,name="create-msme"),
    path('update-msme/<int:pk>/<int:msme_pk>', views.update_msme,name="update-msme"),
    path('delete-msme/<int:pk>/<int:msme_pk>', views.delete_msme,name="delete-msme"),
    # Gst urls
    path('create-gst/<int:branch_pk>', views.create_gst,name="create-gst"),
    path('update-gst/<int:branch_pk>/<int:gst_pk>', views.update_gst,name="update-gst"),
    path('delete-gst/<int:branch_pk>/<int:gst_pk>', views.delete_gst,name="delete-gst"),


    # path('notes/<int:pk>', views.get_single_note,name="notes"),
    
]







