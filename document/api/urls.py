
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

    # branch detail
    path('branch-details/<int:branch_pk>', views.branch_details,name="branch-details"),

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

    # sales invoice
    path('create-sales/<int:branch_pk>',views.create_sales_invoice,name="create-sales"),
    path('edit-sales/<int:branch_pk>/<int:sales_pk>',views.update_sales_invoice,name="edit-sales"),
    path('delete-sales/<int:branch_pk>/<int:sales_pk>',views.delete_sales_invoice,name="delete-sales"),

    # purchase invoice
    path('create-purchase/<int:branch_pk>',views.create_purchase_invoice,name="create-purchase"),
    path('edit-purchase/<int:branch_pk>/<int:purchase_pk>',views.update_purchase_invoice,name="edit-purchase"),
    path('delete-purchase/<int:branch_pk>/<int:purchase_pk>',views.delete_purchase_invoice,name="delete-purchase"),

    # Credit Note
    path('create-credit-note/<int:branch_pk>/<int:sales_pk>',views.create_credit_note,name="create-credit-note"),
    path('update-credit-note/<int:branch_pk>/<int:sales_pk>/<int:cr_pk>',views.update_credit_note,name="update-credit-note"),
    path('delete-credit-note/<int:branch_pk>/<int:sales_pk>/<int:cr_pk>',views.delete_credit_note,name="delete-credit-note"),
    path('view-credit-note/<int:branch_pk>/<int:sales_pk>',views.credit_note_view,name="view-credit-note"),

    # Debit Note
    path('create-debit-note/<int:branch_pk>/<int:purchase_pk>',views.create_debit_note,name="create-debit-note"),
    path('update-debit-note/<int:branch_pk>/<int:purchase_pk>/<int:db_pk>',views.update_debit_note,name="update-debit-note"),
    path('delete-debit-note/<int:branch_pk>/<int:purchase_pk>/<int:db_pk>',views.delete_debit_note,name="delete-debit-note"),
    path('view-debit-note/<int:branch_pk>/<int:purchase_pk>',views.debit_note_view,name="view-debit-note"),
    # path('edit-sales/<int:branch_pk>/<int:sales_pk>',views.update_sales_invoice,name="edit-sales"),
    # path('delete-sales/<int:branch_pk>/<int:sales_pk>',views.delete_sales_invoice,name="delete-sales"),


    # path('notes/<int:pk>', views.get_single_note,name="notes"),
    # bank statement 
    path('create-bank-statement/<int:pk>', views.create_bank_statement,name="create-bank-statement"),
    path('update-bank-statement/<int:pk>/<int:bs_pk>', views.update_bank_statement,name="update-bank-statement"),
    path('delete-bank-statement/<int:pk>/<int:bs_pk>', views.delete_bank_statement,name="delete-bank-statement"),

    # investment certificate
    path('create-interest-certificate/<int:pk>', views.create_interest_certificate,name="create-interest-certificate"),
    path('update-interest-certificate/<int:pk>/<int:ic_pk>', views.update_interest_certificate,name="update-interest-certificate"),
    path('delete-interest-certificate/<int:pk>/<int:ic_pk>', views.delete_interest_certificate,name="delete-interest-certificate"),   

    # Asset Purchased
    path('create-asset-purchased/<int:pk>', views.create_asset_purchased,name="create-asset-purchased"),
    path('update-asset-purchased/<int:pk>/<int:ap_pk>', views.update_asset_purchased,name="update-asset-purchased"),
    path('delete-asset-purchased/<int:pk>/<int:ap_pk>', views.delete_asset_purchased,name="delete-asset-purchased"),   

    # Loan Voucher
    path('create-loan-voucher/<int:pk>', views.create_loan_voucher,name="create-loan-voucher"),
    path('update-loan-voucher/<int:pk>/<int:lv_pk>', views.update_loan_voucher,name="update-loan-voucher"),
    path('delete-loan-voucher/<int:pk>/<int:lv_pk>', views.delete_loan_voucher,name="delete-loan-voucher"),   

    # Tds Certificate
    path('create-tds-certificate/<int:pk>', views.create_tds_certificate,name="create-tds-certificate"),
    path('update-tds-certificate/<int:pk>/<int:tc_pk>', views.update_tds_certificate,name="update-tds-certificate"),
    path('delete-tds-certificate/<int:pk>/<int:tc_pk>', views.delete_tds_certificate,name="delete-tds-certificate"),   

    # Tds Certificate
    path('create-as26/<int:pk>', views.create_as26,name="create-as26"),
    path('update-as26/<int:pk>/<int:as_pk>', views.update_as26,name="update-as26"),
    path('delete-as26/<int:pk>/<int:as_pk>', views.delete_as26,name="delete-as26"),   

    # Investment Statement
    path('create-investment/<int:pk>', views.create_investment,name="create-investment"),
    path('update-investment/<int:pk>/<int:is_pk>', views.update_investment,name="update-investment"),
    path('delete-investment/<int:pk>/<int:is_pk>', views.delete_investment,name="delete-investment"),   

    # Tax Return
    path('create-tax-return/<int:pk>', views.create_tax_return,name="create-tax-return"),
    path('update-tax-return/<int:pk>/<int:tr_pk>', views.update_tax_return,name="update-tax-return"),
    path('delete-tax-return/<int:pk>/<int:tr_pk>', views.delete_tax_return,name="delete-tax-return"),   
    

]







