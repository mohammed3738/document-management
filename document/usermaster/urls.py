from django.urls import path
from usermaster import views


urlpatterns = [
    path('create-vendor/<int:pk>', views.create_vendor,name="create-vendor"),
    path('vendor-detail/<int:vendor_pk>', views.vendor_details,name="vendor-detail"),
    path('create-branch-vendor/<int:pk>', views.create_vendor_branch,name="create-branch-vendor"),
]